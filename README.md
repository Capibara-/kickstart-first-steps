<h1>First steps in Scala</h1>
* <b>Case classes</b>:
    * Free factory method (MyClass.apply(args) = { new MyClass(args) }),
        can instantiate using:
          1. val v = MyClass(argument)
          2. val v = new MyClass(argument)

    * The fields become public parametric fields (like adding val before field
    name in constructor parameter list).

    * Free equals, hashCode, toString.

    * Free copy constructor, can create a new (possibly modified) immutable copy using:
          val v = new MyClass(argument)
          val u = v.copy(arg = newarg)

    * The companion object singleton also gets a method called upapply()
        which returns a Tuple that contains all of the fields of that object
        (up to 22 fields because Function22/Tuple22).

    * The companion object singleton also contains a method called tupled()
        which takes a tuple containing valid (typewise) values for each field
        in the class and returns an instance with those fields.

* A trait can be used to extend or modify behavior of a class quite easily, simply
    override the desired function (when modifying behavior) with the desired implementation
    and add a "with" statement to the class definition. This can even be done for a specific
    instance at runtime, when instantiating use:
        "new MyClass with MyTrait1 with MyTrait2"

* A companion object has access to the class's private members and vice-versa.

* Three imports happen automatically for every source file:
      1. java.lang._
      2. scala._
      3. Predef._ (types, methods, implicit conversions, etc...)
     
*   Extension methods can be written using the implicit keyword which will make
    the class available to implicit conversion. The class defined has to be a value
    class and extend AnyVal (reduces run-time overhead since it is turned to static
    calls behind the scenes).
    
* When creating a class that extends 2 traits (or more) the last trait that is
  mentioned in the class definition is the first one whose methods will be called
  when multiple inheritance is used. This is done by deciding which trait method
  will be called when calling super when USED and not when compiled (which is
  how classes determine calls to super).