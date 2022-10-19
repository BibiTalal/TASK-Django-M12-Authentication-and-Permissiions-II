Haven't seen a movie for a while?

## Steps

## Setup

1. Fork and clone [this repository](https://github.com/malthunayan/TASK-Django-M12-Authentication-and-Permissions-II).
2. Install the `requirements` using `pip install -r requirements/dev.lock`.

## Registration

1. Create a new app called `users`. We will use it for the register, sign in and sign out.
2. Add a `forms.py` file inside of your `users` app.
3. Add a `RegistrationForm` model form.
   - Make sure to set the model equal to `User`, but do not import your `User` model directly (use `Django`'s helper `get_user_model`, which you can read about [here](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#referencing-the-user-model)).
   - Add a widget for the password field to be hidden (you can read about widgets [here](https://docs.djangoproject.com/en/4.0/ref/forms/widgets/)).
4. Add your `register_user` view in `users/views.py`.
   - Create a new instance of your `RegistrationForm`.
   - Check if the `request method` is `POST`. If so, create a new instance of `RegistrationForm` with the first argument passed as `request.POST`.
     - Check if the `form` is `valid`. If so, save the form, but do not commit (i.e., `commit=False`), and assign the return to a variable called `user`.
     - Use `user.set_password` to set the password.
     - Finally, use `user.save` to commit your changes.
     - Then, use the `login` helper to log in (read about it [here](https://docs.djangoproject.com/en/4.0/topics/auth/default/#how-to-log-a-user-in)).
     - `Redirect` to `home`.
   - Create your `context` and add your `form` instance to it.
   - `Render` a template called `register.html`.
5. Add your `register_user` view to `urls.py` and name it `register`.
6. Add the `register.html` template to `users/templates` (you can use `crispy forms` and `bootstrap` to prettify it).
7. Add a link to `register` in the navbar of `shared/templates/home.html` and `movies/template/movie_list.html`.
8. Right now, we have no way to tell that we are registered and logged in other than trying to register again and failing. We will see how we can make it visible to the users that they're logged in in the upcoming task. Commit and push your changes.

## Logout

1. Add a `logout_user` view that uses the `logout` [helper](https://docs.djangoproject.com/en/4.0/topics/auth/default/#how-to-log-a-user-out) from `Django`.
2. Add the `logout_user` view to `urls.py` with the name `logout`.
3. Add a condition in the navbars (`shared/templates/home.html`, `movies/templates/movie_list.html`, etc...) that checks if the `user` is `authenticated`.
   - If the user is authenticated, show the `anchor` tag that will log them out.
   - Else show the registration link.
4. Commit and push your code.

## Login

1. Add the `LoginForm` in `users/forms.py` that inherits from `Form`, not from `ModelForm`.
   - `username`: `CharField` which is `required`
   - `password`: `CharField` which is `required` and has a `PasswordInput` widget (read about widgets [here](https://docs.djangoproject.com/en/4.0/ref/forms/widgets/))
2. Add the `login_user` view in `users/views.py`.
   - Create a new `form` instance of `LoginForm`.
   - Check if the `request method` is `POST`, if so:
     - Create a new `form` instance of `LoginForm` with the first argument as `request.POST`.
     - Check if the `form` is `valid`, if so:
       - Authenticate the user using the `authenticate` [helper](https://docs.djangoproject.com/en/4.0/topics/auth/default/#authenticating-users) from `Django`, which will use the `cleaned_data` from the `form` instance we last created, and assign the return from this helper to a variable called `auth_user`
       - Check if `auth_user` is **not** `None`, if so:
         - Use the `login` helper from `Django` to log in and `redirect` to `home`.
   - Create your `context` and add the `form` instance to it.
   - `Render` your `request`, `login.html` template, and `context`.
3. Add the `login_user` view to `urls.py` with the name `login`.
4. Add the `login` template in `users/templates/login.html` (you can use `crispy forms` and `bootstrap` to prettify it).
5. Update all navbars (`shared/templates/home.html`, `movies/templates/movie_list.html`, etc...) to include the link to `login`.
   - Make sure the link only appears if the user is anonymous (i.e., not logged in).
6. Add an `anchor` tag inside your `login.html` template to link new users to the `registration` form.
7. Add an `anchor` tag inside your `register.html` template to link old users to the `login` form.
8. Try out the `login` form.
9. Commit and push your code.

## Permissions

1. Add `LOGIN_URL` to your `settings.py` to be equal to whatever path you've added as your `login` (read more about this [here](https://docs.djangoproject.com/en/4.0/ref/settings/#login-url)).
2. We want to add an `anchor` tag to our `create-movie` link (the view and template have already been created).
   - Add this link in the `movie-list` page somewhere, but add a condition in the template so that it only appears if the user logs in.
3. Try going to the link directly (e.g., `http://localhost:8000/movies/add/`), and you'll notice that users are still able to go to it.
4. Add a `login_required` decorator to `create_movie` view in `movies/views.py`.
   - Read about the decorator [here](https://docs.djangoproject.com/en/4.0/topics/auth/default/#the-login-required-decorator).

### Bonus

1. If you go to `movies/views.py` and see the `create_movie` view, you'll notice a _bonus_ comment. If you try to create a movie, even if you're logged in, it won't actually work. The reason is that the `form` expects to have `created_by` injected into it during runtime. We need to add the `request.user` to the form defaults for `created_by` in order for our view to work. Read about form defaults [here](https://docs.djangoproject.com/en/4.0/ref/forms/api/#initial-form-values).
2. Customize your `User` model by inheriting from `django.contrib.auth.models.AbstractUser`. Go to `settings.py` and add `AUTH_USER_MODEL = "users.User"`, where `users` is the app name and `User` is the class name we chose for our custom `User` model. Don't forget to make migrations and migrate.
# -TASK-Django-M12-Authentication-and-Permissiions-II
# TASK-Django-M12-Authentication-and-Permissiions-II
