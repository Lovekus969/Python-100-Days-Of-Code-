
// Swift basics: variables, loops, and functions

import Foundation

// --- Variables ---
var name: String = "Kush"
let age: Int = 21   // 'let' means constant (like final in Java)

print("Name:", name)
print("Age:", age)

// --- Dynamic typing in Swift? ---
// Swift is statically typed (not like Python).
// You can omit type, Swift will infer it:
var city = "Toronto"
var height = 5.9

print("City:", city)
print("Height:", height)

// --- For Loop ---
print("\n--- For Loop Example ---")
for i in 1...5 {
    print("Number:", i)
}

// --- Array Loop ---
let fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits {
    print("I like \(fruit)")
}

// --- Function ---
func greet(person: String) -> String {
    return "Hello, \(person)!"
}

print("\n" + greet(person: "Kush"))
