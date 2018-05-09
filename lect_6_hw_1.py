import requests

# requests for /roles

full_url_roles = "http://pulse-rest-testing.herokuapp.com/"

data_new_role = {"name": "Hanna", "type": "Hero", "book": 13, "level": 1}
post_response = requests.post(full_url_roles + "roles/", data=data_new_role)

print(post_response.json())
person = post_response.json()
person_id = person['id']

print(person_id)

get_response = requests.get(full_url_roles + "roles/" + str(person_id))
print(get_response.text)


get_response = requests.get(full_url_roles + "roles/")
users_list = get_response.json()
print(users_list)

for user in users_list:
    if user["id"] == person_id:
        print(user)

book_id = 1
put_response = requests.put(full_url_roles + "roles/" + str(person_id), data= {"book": book_id})
print(put_response.json())


get_response = requests.get(full_url_roles + "roles/" + str(person_id))
print(get_response.json())

person = get_response.json()

if person["book"] == book_id:
    print(person)

get_response = requests.get(full_url_roles + "roles/")
users_list = get_response.json()

for new_person in users_list:
    if new_person["id"] == person_id and new_person["book"] == book_id:
        print(new_person)

delete_response = requests.delete(full_url_roles + "roles/" + str(person_id))
print(delete_response.status_code)

get_response = requests.get(full_url_roles + "roles/" + str(person_id))
print(get_response.status_code)




# requests for /books

full_url_books = "http://pulse-rest-testing.herokuapp.com/"

data_new_book = {"title": "NSO book", "author": "n s o"}
post_response = requests.post(full_url_books + "books/", data=data_new_book)

print(post_response.json())
new_book = post_response.json()
book_id = new_book['id']

print(book_id)

get_response = requests.get(full_url_books + "books/" + str(book_id))
print(get_response.text)


get_response = requests.get(full_url_books + "books/")
books_list = get_response.json()
print(books_list)

for book in books_list:
    if book["id"] == book_id:
        print(book)

change_book_title = "nso new book"
put_response = requests.put(full_url_books + "books/" + str(book_id), data={"title": change_book_title})
print(put_response.json())

get_response = requests.get(full_url_books + "books/" + str(book_id))
print(get_response.json())

new_book = get_response.json()

if new_book["title"] == change_book_title:
    print(new_book)

get_response = requests.get(full_url_books + "books/")
books_list = get_response.json()

for check_new_book in books_list:
    if check_new_book["id"] == book_id and check_new_book["title"] == change_book_title:
        print(check_new_book)

delete_response = requests.delete(full_url_books + "books/" + str(book_id))
print(delete_response.status_code)

get_response = requests.get(full_url_books + "books/" + str(book_id))
print(get_response.status_code)

