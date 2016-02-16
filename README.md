# Hackathon 2016

Using Cortical.io’s Natural Language Processing API, automatically sort emails, tickets, reviews, descriptions, etc. into categories rather than relying human interaction.
### REQUIREMENTS / SETUP

-  To use, ensure you have a file called apiStorage.py to contain your api key.
   Use vi to open .gitignore and add the line "apiStorage.py". (This will prevent you from accidentally uploading your api key)

-  You'll need to install the retinasdk:
   pip install retinasdk
   (For obtaining pip, see https://pip.pypa.io/en/stable/installing/ )

### Comments

I grabbed a few samples from yelp reviews, amazon reviews, and League of Legends bugs/issues discussion boards for negative and positive reviews, and bug/issue reports. The amount of samples I have are quite limited (see dataset directory), and the baseline we created for the negReviews, posReviews, and issues were also small. Perhaps these factors can explain the poorly categorized samples? 

Welp, input2.list seemed better categorized than input1.list. ( run python on demo.py to see the categorization in action)
