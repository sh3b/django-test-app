# django-test-app
A simple Django test app with Group/Permissions/Restricted Views.

1. Create a virtualenv
2. pip install -r requirements.txt
3. python manage.py runserver


## Testing Restrcited Views
1. Login with user1 and password '12346' 
2. Go to: http://127.0.0.1:8000/view-1/ it should return 'This is View 1'
   and http://127.0.0.1:8000/view-2/ should redirect to login page. Login with user 'user2' and password '123456'.



## Users 

admin / 123456

user1 / 123456

user2 / 123456


## Tests

You can also run tests with 'python manage.py test' instead of checking the views manually.
