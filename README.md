# Translation-Style-Sheet-Enforcer
Enforces Translation Style Sheet on txt
***

1. Place your original text in Japanese into the "input" folder as "jp.txt" (plain text file)
2. Place your style sheet also into the "input" folder as "ss.csv" (CSV file)
  - The CSV file should only have 2 columns, with the Japanese text in the first column and the English translation on the second
    - e.g. "日本語, Japanese"
3. Run the script "main.py"
  - Mac users can use the "__`Start.command" file to run the script
  - Windows users: I'M SORRY!
4. The final product will appear in the "output" folder
***

Note:
- This is a very crude programme, which means:
  - It will definitely miss some terms in the text that does not appear exactly as is in the CSV file provided
    - Which means you should really make a very clean version of the CSV
  - Japanese names should be separated by the "・" symbol between first/last names, English separated by a space. The order of the names should also be the same in both languages
  - The script will sometimes generate weird results if the same term existed multiple times in the CSV file. It'll basically be a list of all the translations provided in the CSV, you'll have to choose which one to use.