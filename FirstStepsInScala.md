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
          

    * The companion object singleton also gets a method called `upapply()`
        which returns a `Tuple` that contains all of the fields of that object
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
          `::` (rather than constructor matching with a wildcard).

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

* **Actors (DEPRECATED)**:
  		
  	* Analogous to Thread in Java, implement run() and it will run in it's own
        thread.

   * Defined as object.
   
   * It is also possible to `import scala.actors.Actor._` and do:
   
	    ```
          val myObj = actor {
            // Do work.
          }
		```
		
   * To define a handler function for message receiving for an actor
        use receive() that takes a function f: Any -> Unit and issue a message
        to an actor like this:

          `myActor ! myMsg`

        the message itself can be of any type.

   * Every actor has an inbox (message queue). The inbox is inherently
        thread safe. The ! method simply inserts a message into the inbox
        and returns. It is not good practice to pass as argument to ! a
        mutable object since it will require synchronization on that object.

   * Since an actor has a mutable state, if you pass an argument to ! that
        is not handled in the case match that is the body of receive it will
        wait in the inbox until timeout or until the actor changes behaviour
        and is able to handle that type.

   * To get a `Future[T]` as an immediate response back from an Actor use:
          `myActor ? myMsg'
                    
   * In order to get immidiate (blocking) result use:
  
	```
  		implicit val timeout = Timeout(5 seconds)
  		val f1 = myActor ? myMsg
  		Await.result(f1, timeout.duration)
	```
	
	* To send a message back to the sender use `sender ! returnVal` inside the receive method.



* **Future**:

  * Calling `map()` on a `Future[T]` does not block but returns a new `Future[T1]`,
      you need to either specify the execution context (thread pool being used) or
      import `scala.concurrent.ExecutionContext.Implicits.global` for the global thread
      pool to be used implicitly.
  
  * Calling `future` on a piece of code tells the Scala scheduler to run that code
    on a different thread. What returns is a box that will contain the value of
    the computation SOMETIME later.
    
  * Don't use .get() on a Future, it can cause a blocking operation.

  * Future offers a few tools that enable work without blocking:
    .map(), .flatMap(), .filter(), onComplete(), onSuccess(), onFailure().
    
  * Every instance of `Future[T]` has an instance of `Promise[T]`.

  * `Promise[T]` has 2 functions, 1 for success and 1 for failure, that are called
    when the computation is finished. This in turn calls then `onSuccess/onFailure` 
    and `onCompleted` of the associated `Future[T]`. These success and failure 
    functions are called when using `future()` on a piece of code.
    
  * A `.map()` on a `Future[T]` that threw an exception during computations will return the same `Future[T]` filled with the exception.
  
  * A `Future[T]` can be in 1 of three states: not done yet, done, threw an exception.
  
  * Future offers a few tools that enable work without blocking:
    `.map(), .flatMap(), .filter(), onComplete(), onSuccess(), onFailure().`

  * A .map() on a Future[T] that threw an exception during computations will
    return a Future[T] filled with the exception.
          
* A trait can be used to extend or modify behavior of a class quite easily, simply
    override the desired function (when modifying behavior) with the desired implementation
    and add a "with" statement to the class definition. This can even be done for a specific
    instance at runtime, when instantiating use:
        `new MyClass with MyTrait1 with MyTrait2`

* A companion object has access to the class's private members and vice-versa.

* It is possible to import objects (which will bring all methods and members
    into the namespace):
	
	```
		val obj = new MyObject
		import obj._
	```
	
    This also works for singleton objects.
    
* You can rename a package when importing (like python's "import A.b as B"): `import A.{ b => B }`. This will hide the original name so A.b is no longer accessible.

* It is also possible to exclude a specific sub-package from being imported when importing the entire package: `import A.{WilNotBeImported => _, _}`.

* When working with `Option[T]` foreach is eagerly evaluated and does not return
    a value while `map()` is lazily evaluated and does return a value.
    
* It is possible to define functions inside other classes/functions and avoid creating a private method.

* A `foreach` with a lambda function that has a case match in it that covers
    the entire domain of the is identical to a `foreach` without a lambda but with
    a case match that covers the entire domain (partial function to total
    function conversion).
    
* Calling `future` on a piece of code tells the Scala scheduler to run that code
    on a different thread. What returns is a box that will contain the value of
    the computation SOMETIME later.


