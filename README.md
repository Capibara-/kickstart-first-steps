<h1>First steps in Scala</h1>
* **Case classes**:
    * Free factory method (`MyClass.apply(args) = { new MyClass(args) }`), can instantiate using:
   		1. `val v = MyClass(argument)`
      	2. `val v = new MyClass(argument)`

    * The fields become public parametric fields (like adding val before field
    name in constructor parameter list).

    * Free `equals, hashCode, toString`.

    * Free copy constructor, can create a new (possibly modified) immutable copy using:

    
	    ```
	    val v = new MyClass(argument);
	    val u = v.copy(arg = newarg)
	    ```
          

    * The companion object singleton also gets a method called upapply()
        which returns a Tuple that contains all of the fields of that object
        (up to 22 fields because `Function22/Tuple22`).

    * The companion object singleton also contains a method called tupled()
        which takes a tuple containing valid (typewise) values for each field
        in the class and returns an instance with those fields.
        

* **Pattern Matching**:
      * When using pattern matching a variable name starting with a capital letter
          is treated as a constant and not a variable.

      * Constructor parameters: It is possible to match a constructor call
          with a variable, the match will occur if the object can be constructed
          using that specific case (can be used in conjunction with wildcard).

      * When matching a sequence pattern it is idiomatic in Scala to use
          "::" (rather than constructor matching with a wildcard).

      * Using tuple patterns it is possible to de-structure a list (or tuple)
          using:
          
          ```
          val List(a,b,c) = myList
          val (a,b,c) = myTuple
          ```
          

      * It is also possible to match by the type of the object being matched.

      * The JVM does type erasure so matching a Map with concrete key and values
          (rather than wildcards/vars) types will return true regardless of the concrete types.

      * It is possible to bind a variable inside a match using `@`:
             
              expr match {
                case List(1, e @ 2) => e*2
                _ => -1
              }
              

      * It is possible to include an if in a case match.

      * When defining a sealed class extending it is only possible in The
          same .scala file. Also when using a sealed class the compiler will
          throw compile errors when a match is not exhaustive.

      * It is possible to de-construct an `Option[T]` using:
          
          ```
          Some(s) => s
          None => "wtf"
          ```

      * It is possible to define variables using patterns (similar to constructor
          parameters):
          
              
              val exp = new MyClass(p1, p2, p3)
              val MyClass(a1, a2, a3) = exp
              
          Will bind a1, a2, a3 to p1, p2, p3.

      * It is possible to use pattern matching in for expressions to iterate
          over all key-value pairs os a `Map[T1,T2]`.

* **Future**:

  * Calling map() on a `Future[T]` does not block but returns a new `Future[T1]`,
      you need to either specify the execution context (thread pool being used) or
      import `scala.concurrent.ExecutionContext.Implicits.global` for the global thread
      pool to be used implicitly.

  * Interesting callback methods: `onComplete, onFailure, onSuccess`.

  * Interesting methods: `isCompleted`.      
          
* A trait can be used to extend or modify behavior of a class quite easily, simply
    override the desired function (when modifying behavior) with the desired implementation
    and add a "with" statement to the class definition. This can even be done for a specific
    instance at runtime, when instantiating use:
        `new MyClass with MyTrait1 with MyTrait2`

* A companion object has access to the class's private members and vice-versa.
