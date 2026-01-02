# django-simple-feedback

django-simple-feedback is a Django app to get a feedback from users.
Users input their email (optionally) and message (required) in form.
Administrator can view feedbacks and change its status.


Quick start
-----------

1. Add "feedback" to your INSTALLED_APPS setting like this::
    ```
    INSTALLED_APPS = [
        ...,
        "django_simple_feedback",
    ]
    ```

2. Include the feedback URLconf in your project urls.py like this::
    ```
    path("feedback/", include("django_simple_feedback.urls")),
    ```

3. Run ```python manage.py migrate``` to create the models.

4. Start the development server and visit the admin to create a feedback.

5. Visit the ```feedback/``` URL to see the feedback form.
