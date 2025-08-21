
# Ruby basics continued: arrays, hashes, loops, classes, and blocks

# --- Arrays ---
numbers = [1, 2, 3, 4, 5]
puts "\nSquares of numbers:"
numbers.each do |num|
  puts "#{num} squared is #{num * num}"
end

# --- Hashes (like Python dict) ---
person = {
  "name" => "Kush",
  "age" => 21,
  "city" => "Toronto"
}

puts "\nPerson Hash:"
person.each do |key, value|
  puts "#{key.capitalize}: #{value}"
end

# --- While Loop ---
puts "\nCounting with while:"
i = 1
while i <= 5
  puts "Count: #{i}"
  i += 1
end

# --- Class (OOP in Ruby) ---
class Student
  attr_accessor :name, :age

  def initialize(name, age)
    @name = name
    @age = age
  end

  def intro
    "Hi, I am #{@name}, and I am #{@age} years old."
  end
end

student1 = Student.new("Kush", 21)
puts "\n" + student1.intro

# --- Blocks (very Ruby feature) ---
puts "\nUsing a block to repeat an action:"
3.times do |i|
  puts "This is loop ##{i+1}"
end
