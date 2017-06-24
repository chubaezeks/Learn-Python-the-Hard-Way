


soup = BeautifulSoup(html)
type(soup) #still need to figure out why we're doing this? to define as an object or just to check to see what type of object it is?

soup.findAll('tr', limit=2)
soup.findAll('tr', limit=2)[1]
soup.findAll('tr',limit=2)[1].findAll('th')

column_headers = [th.getText() for th in soup.findAll('tr',limit=2)[1].findAll('th')]

column_headers # our column headers

data_rows = soup.findAll('tr')[2:] #skip the first two rows

type(data_rows) #This gives us a list of table rows, but how and why? Is data_row itself a categorization?


#why is the row described as a 2 dimensional matrix and what the heck does that mean?
#what is a nested list comprehension?
player_data = [[td.getText() for td in data_rows[i].findAll('td')] for i in range(len(data_rows))]

#The outer for loop extracts the rows and the inner for loop extracts the text from each row
