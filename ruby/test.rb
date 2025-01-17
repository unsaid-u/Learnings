# ruby is a dynamically typed, interpreted, purely OOP lang
# everything in an object in ruby

puts "Hello world"

# data types
# operators
# loops

name = "utkarsh"
last_name = "jain"

puts name.class

puts name + last_name
puts "#{name} #{last_name} --- string interpolation or templating"

# hashes --- like dict or obj in python and js
dict = {
    string: "string",
    number: 12,
    boolean: false,
    null: nil,
    array: [12,13,"name",nil],
    symbol: :"ruby_symbol"      # are basically immutable strings
}

puts "data types in ruby \n #{dict}"

# range operator
    # to_a to convert to array
puts (1..4)         # inclusive range   output : 1..4
puts (1..4).to_a
puts (12...15).to_a # exclusive range

# defined operator 
puts defined?(x)       # "nil" if x is undefined
puts defined?(puts)    # "method"

# safe navigation - like optional chaining in js (?.)
user = nil
puts user&.name  # Avoids raising NoMethodError

# nil data type with if check 
x = nil
if x.nil?
  puts "x is nil"
end


=begin
 Multiline comment in ruby 


* unless condition
    Code to execute if condition is false
   end


   unless condition
  # Code to execute if the condition is false
else
  # Code to execute if the condition is true
end


* until condition
    Code will execute until condition is false
  end

* for i in 1..5
  puts i
end
    for variable in range
  # Code to execute
end


* break
* next --- continue
* redo 


=end 



# ? Preferred: Methods like each, map, select, inject are more common and are considered more idiomatic Ruby.
# ! Less Common: for loops are used, but they are less idiomatic and typically replaced by enumerator methods for clarity and expressiveness.


def method_name(parameter1, parameter2)
    # method body
    value = 12
    return value  # (optional as Ruby returns last evaluated expression by default)
  end
  

# arrow functions in ruby 
lambda_function = ->(x, y) { x + y }
puts lambda_function.call(3, 4)  # Output: 7

shorthand_method = ->(param="default Value") {
    puts param
    return param + "from return"
}

puts shorthand_method.call()        # for calling use .call method 

# a class explaining scopes
class MyClass
    @@class_var = 100  # Class variable
    CONSTANT_VAR = "I'm a constant"  # Constant
  
    def initialize(value)
      @instance_var = value  # Instance variable
    end
  
    def display
      local_var = "I'm local"  # Local variable
      puts "Instance Variable: #{@instance_var}"
      puts "Class Variable: #{@@class_var}"
      puts "Constant Variable: #{CONSTANT_VAR}"
      puts "Local Variable: #{local_var}"
    end
  end
  
  obj = MyClass.new(50)
  obj.display
  

x = 23
y = x 

puts x , y

x = 43
puts x , y
