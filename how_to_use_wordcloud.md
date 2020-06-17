### how to use wordcloud

from PIL import Image  
import requests  
from io import BytesIO  

#### 1. only generate wordcloud  
#### Create and generate a word cloud image:  
wordcloud = WordCloud().generate(text)  
#### Display the generated image:  
plt.imshow(wordcloud, interpolation='bilinear')  
plt.axis("off")  
plt.show()  

#### 2. generate wrodcloud based a picture  
response = requests.get(url)  
img = Image.open(BytesIO(response.content))  
maskArray = np.array(Image.open(BytesIO(response.content)))  
#### Generate a word cloud image  
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)  
