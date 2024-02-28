Templates inheritance:
-------------------------
The process of deriving the features of one template (html page) to other template
(html page) is called as template inheritance.

Whenever we work with respect to the real time application there are many features like top bar, navigation bars, footer bar, some others features, will be same in the each and 
every templates (html file). Instead of repeating the code again and again we came up with the concept of templates inheritance and we utilizing in all the situations.

If one project multiple templates files have some common code, it is not recommended to write that common code in every template html file. It increases length of 
the code and reduces readability. It also increases development time.

We have to separate that common code into a new templates file, which is also known as base template html file. The remaining template files should required extending base 
template so that the common code will be inherited automatically.

Inheriting common code from base templates to remaining templates is nothing but template inheritances.

Templates inheritances tags:
---------------------------
Extends jinja tag:
        {% extends “filename_with_path .extension” %} 
In general, extend a file to use its code as a base for multiple templates

