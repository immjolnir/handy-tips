# Tips for Groovy

## exam-map.get
```
public Object get(Object key, Object defaultValue)
```
Looks up an item in a Map for the given key and returns the corresponding value.

If there is no entry for the given key return instead the default value and also add the key and default value to the map.

For a method which doesn't mutate the map, consider instead using Map#getOrDefault(Object, Object) or consider using Groovy's MapWithDefault often instantiated using Map#withDefault(Closure) or with more options Map#withDefault(boolean, boolean, Closure).

