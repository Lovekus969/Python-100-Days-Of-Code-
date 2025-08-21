
// More Swift basics: conditionals, while loop, optionals

import Foundation

// --- Conditionals ---
let score = 85

if score >= 90 {
    print("Grade: A")
} else if score >= 75 {
    print("Grade: B")
} else {
    print("Grade: C")
}

// --- While Loop ---
print("\n--- While Loop Example ---")
var i = 1
while i <= 5 {
    print("Counting:", i)
    i += 1
}

// --- Optionals ---
// Swift has "Optionals" for variables that might have no value
var nickname: String? = nil  // currently no value
print("\nNickname is:", nickname as Any)

// Later we assign a value
nickname = "BeeBa"
print("Nickname is:", nickname!)

// Safe way (Optional Binding)
if let safeName = nickname {
    print("Unwrapped Nickname:", safeName)
} else {
    print("No nickname found")
}

// --- Function with default parameter ---
func multiply(a: Int, b: Int = 2) -> Int {
    return a * b
}

print("\nMultiply 5 by default b (2):", multiply(a: 5))
print("Multiply 5 by 3:", multiply(a: 5, b: 3))
