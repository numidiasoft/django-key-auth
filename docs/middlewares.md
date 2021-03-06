# Middlewares

## KeyAuthenticationMiddleware

Middleware to authenticate user through given key. (Required)

```python
MIDDLEWARE_CLASSES = (
    ...
    'keyauth.middleware.KeyAuthenticationMiddleware',
)
```

This middlware adds two attributes to the `request` object:

- `request.user`: `User` instance of the authenticated client.
- `request.key`: `Key` instance of the given token.


## KeyRequiredMiddleware

Add this middleware to protect all views with key authetication.

```python
MIDDLEWARE_CLASSES = (
    ...
    'keyauth.middleware.KeyRequiredMiddleware',
)
```

## SuitableKeyMiddleware

Add this middleware to check if given key is suitable according to its type and request's user agent.

```python
MIDDLEWARE_CLASSES = (
    ...
    'keyauth.middleware.KeyRequiredMiddleware',
    'keyauth.middleware.SuitableKeyMiddleware',
)
```
