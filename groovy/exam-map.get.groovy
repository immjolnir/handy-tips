
def map=[:]
map.get("a", []) << 5
assert map == [a:[5]]

def m0 = ["a": 1, "b": 2]

def av = m0.get("a", 0)
def cv = m0.get("c", 0)
assert av == 1
assert cv == 0
println "In the m0, a => ${av}, c => ${cv}"

// See https://docs.oracle.com/en/java/javase/15/docs/api/java.base/java/util/Map.html#getOrDefault(java.lang.Object,V)
// Implementation Requirements:
// The default implementation makes no guarantees about synchronization or atomicity properties of this method. Any implementation providing atomicity guarantees must override this method and document its concurrency properties.
def av2 = m0.getOrDefault("a", 0)
def cv2 = m0.getOrDefault("c", 0)
assert av2 == 1
assert cv2 == 0
println "In the m0, a => ${av2}, c => ${cv2}"

// using  containsKey 
assert m0.containsKey("a")
assert m0.containsKey("c")
