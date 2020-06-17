### Target: download all of the movie poster images for the Roger Ebert review word clouds.

There are two key things to be aware of before you begin:

* 1. Wikipedia Page Titles
To access Wikipedia page data via the MediaWiki API with wptools (phew, that was a mouthful), you need each movie's Wikipedia page title, i.e., what comes after the last slash in en.wikipedia.org/wiki/ in the URL. For this lesson, I've compiled all of these titles for each of the movies in the Top 100 for you.
* 2. Downloading Image Files
Downloading images may seem tricky from a reading and writing perspective, in comparison to text files which you can read line by line, for example. But in reality, image files aren't special—they're just binary files. To interact with them, you don't need special software (like Photoshop or something) that "understands" images. You can use regular file opening, reading, and writing techniques, like this:  

'''  

import requests  

r = requests.get(url)  

with open(folder_name + '/' + filename, 'wb') as f:  

        f.write(r.content)  
'''
But this technique can be error-prone. It will work most of the time, but sometimes the file you write to will be damaged. 
