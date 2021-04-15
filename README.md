# eesc
Easter Egg Supported Calculator library for Python.
<br/>
## To use it,
To use it, the `eesc.py` file and your Python file should be in the same directory.
## Adding a new language:
If you know another language, you can add support in this way:
1. Add your language's contraction to list `langs`, for example `tr` for Turkish.
2. Copy the key `en` from the dict `translation` and paste it to end of the dict. Don't forget to put a comma before it.
3. Change the new key's name to your language's contraction.
4. Translate the keys' values.
5. Create a pull request!
