Reference commands
==================

Basic tutorial
--------------

To get started on lumache, you will need to start off with setup environment

```console
(venv) $ pip install lumache
```

Advance tutorial
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

```{eval-rst}  
.. autofunction:: lumache.get_random_ingredients
```

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, `python lumache.get_random_ingredients` will raise an exception.

```{eval-rst}
.. autoexception:: lumache.InvalidKindError
```

```{eval-rst}
.. doctest::

    >>> import lumache
    >>> lumache.get_random_ingredients()
    ['shells', 'gorgonzola', 'parsley']
```
