
# Ruby basics: variables, loops, conditionals, function

# --- Variables ---
name = "Kush"
age = 21
height = 5.9
is_student = true

puts "Name: #{name}"
puts "Age: #{age}"
puts "Height: #{height}"
puts "Student: #{is_student}"

# --- Conditionals ---
score = 85

if score >= 90
  puts "Grade: A"
elsif score >= 75
  puts "Grade: B"
else
  puts "Grade: C"
end

# --- For Loop ---
puts "\n--- For Loop Example ---"
for i in 1..5
  puts "Number: #{i}"
end

# --- Each Loop (Ruby style) ---
fruits = ["apple", "banana", "cherry"]
fruits.each do |fruit|
  puts "I like #{fruit}"
end

# --- Function ---
def greet(person)
  return "Hello, #{person}!"
end

puts "\n" + greet("Kush")
