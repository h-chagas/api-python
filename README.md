# api-python

##### Purpose:  
- This API provides consultation, creation, editing and deletion of books.  
- URL base: localhost.  
-  Endpoints:  
    - localhost/books (GET), get all books  
    - localhost/books (POST), create a book  
    - localhost/books/id (GET w/ id), get a book by its id  
    - localhost/books/id (PUT w/ id), modify a book  
    - localhost/books/id (DELETE w/ id), delete a book  
- Resource: Books.  

##### To run this API, you'll need to install:  

###### Python  
> https://www.python.org/  

###### Visual Studio Code  
> https://code.visualstudio.com/  

###### Postman  
> https://www.postman.com/  

###### FLASK
```bash
pip install flask
```  

##### Data source:
As this is a simple API, the data source will be a dictionary:  
```python
books = [
    {
        'id': 1,
        'title': '365 Days of Dad Jokes',
        'author': 'Jim Chumley'
    },
    {
        'id': 2,
        'title': 'Building High Performance Agile Teams',
        'author': 'Made Tech'
    },
    {
        'id': 3,
        'title': 'Moby-Dick',
        'author': 'Herman Melville'
    },
]
```
<br/>  

##### Results  

###### Get all Books (GET)  
<img src='\screenshots\1-get_all_books.png'/>

<br/>

###### Create a Book (POST) 
<img src='\screenshots\2-post_create_a_book.png'/>

<br/>

###### Get a Book by ID (GET)  
<img src='\screenshots\3-get_a_book_by_id.png'/>

<br/>

###### Modify a Book (PUT)  
<img src='\screenshots\4-modify_a_book.png'/>

<br/>

###### Delete a Book (DELETE)  
<img src='\screenshots\5-delete_a_book.png'/>

<br/>

