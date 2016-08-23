#copy from dataquest task

from bs4 import BeautifulSoup

# Initialize the parser, and pass in the content we grabbed earlier.
parser = BeautifulSoup(content, 'html.parser')

# Get the body tag from the document.
# Since we passed in the top level of the document to the parser, we need to pick a branch off of the root.
# With beautifulsoup, we can access branches by simply using tag types as 
body = parser.body

# Get the p tag from the body.
p = body.p

# Print the text of the p tag.
# Text is a property that gets the inside text of a tag.
print(p.text)

title_text = parser.title.text




# Get the page content and setup a new parser.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_ids.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Pass in the id attribute to only get elements with a certain id.
first_paragraph = parser.find_all("p", id="first")[0]
print(first_paragraph.text)

second_paragraph = parser.find_all('p')[1]
second_paragraph_text = second_paragraph.text

first_outer_paragraph = parser.find_all('p', class_='outer-text')[0]
first_outer_paragraph_text = first_outer_paragraph.text


# Get the website that contains classes and ids
response = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Select all the elements with the first-item class
first_items = parser.select(".first-item")

# Print the text of the first paragraph (first element with the first-item class)
print(first_items[0].text)

outer_items = parser.select('.outer-text')
first_outer_text = outer_items[0].text


second_items = parser.select('#second')
second_text = second_items[0].text
