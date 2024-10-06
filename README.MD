## Introduction


## Background


## Tools I Used

### VS Code

### Django


## What I Learned

### Part 1: Requests and responses

### Part 2: Models and the admin site

### Part 3: Views and templates

### Part 4: Forms and generic views

#### Forms:

- **csrf_token**: A security measure to protect web applications from **Cross-Site Request Forgery(CSRF)** attacks.
    - Why? : Prevent Unauthorized Actions, Session Security.
    - By default, Django includes CsrfViewMiddleware in MIDDLEWARE settings in settings.py.
    - Use `{% csrf_token %}` in Templates.
    - Handling Forms in Views: In your views, Handle POST requests as usual. If the CSRF token is missing or invalid, Django will raise a 403 Forbidden error.




### Part 5: Testing

### Part 6: Static files

### Part 7: Customizing the admin site

### Part 8: Adding third-party package

## Conclusion

