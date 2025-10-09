#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

/**
 * Comprehensive C Programming Demo Codes Collection
 * This file contains various C programming examples and demonstrations
 * covering fundamental concepts, data structures, and algorithms
 */

// 1. Basic Data Types and Variables Demo
void dataTypesDemo() {
    printf("=== Data Types Demo ===\n");
    
    // Integer types
    int integer = 42;
    short shortInt = 32000;
    long longInt = 2147483647L;
    long long longLongInt = 9223372036854775807LL;
    
    // Floating point types
    float floatNum = 3.14159f;
    double doubleNum = 3.141592653589793;
    long double longDouble = 3.141592653589793238L;
    
    // Character type
    char character = 'A';
    
    // Boolean (using int)
    int boolean = 1; // 1 for true, 0 for false
    
    printf("Integer: %d\n", integer);
    printf("Short: %hd\n", shortInt);
    printf("Long: %ld\n", longInt);
    printf("Long Long: %lld\n", longLongInt);
    printf("Float: %.5f\n", floatNum);
    printf("Double: %.15f\n", doubleNum);
    printf("Long Double: %.15Lf\n", longDouble);
    printf("Character: %c\n", character);
    printf("Boolean: %s\n", boolean ? "true" : "false");
    printf("\n");
}

// 2. Array Operations Demo
void arrayOperationsDemo() {
    printf("=== Array Operations Demo ===\n");
    
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printf("Original array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    // Find maximum element
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    printf("Maximum element: %d\n", max);
    
    // Calculate sum
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    printf("Sum of elements: %d\n", sum);
    printf("Average: %.2f\n", (float)sum / n);
    
    // Reverse array
    printf("Reversed array: ");
    for (int i = n - 1; i >= 0; i--) {
        printf("%d ", arr[i]);
    }
    printf("\n\n");
}

// 3. String Manipulation Demo
void stringManipulationDemo() {
    printf("=== String Manipulation Demo ===\n");
    
    char str1[] = "Hello";
    char str2[] = "World";
    char result[50];
    
    // String length
    printf("Length of '%s': %zu\n", str1, strlen(str1));
    
    // String concatenation
    strcpy(result, str1);
    strcat(result, " ");
    strcat(result, str2);
    printf("Concatenated: %s\n", result);
    
    // String comparison
    int cmp = strcmp(str1, str2);
    printf("Comparison result: %d\n", cmp);
    
    // String copy
    char copied[20];
    strcpy(copied, str1);
    printf("Copied string: %s\n", copied);
    
    // Character search
    char *found = strchr(str1, 'l');
    if (found) {
        printf("First 'l' found at position: %ld\n", found - str1);
    }
    
    printf("\n");
}

// 4. Pointer Operations Demo
void pointerOperationsDemo() {
    printf("=== Pointer Operations Demo ===\n");
    
    int num = 42;
    int *ptr = &num;
    
    printf("Value of num: %d\n", num);
    printf("Address of num: %p\n", &num);
    printf("Value of ptr: %p\n", ptr);
    printf("Value pointed by ptr: %d\n", *ptr);
    
    // Pointer arithmetic
    int arr[] = {10, 20, 30, 40, 50};
    int *arrPtr = arr;
    
    printf("\nArray using pointers:\n");
    for (int i = 0; i < 5; i++) {
        printf("arr[%d] = %d (address: %p)\n", i, *(arrPtr + i), arrPtr + i);
    }
    
    printf("\n");
}

// 5. Function with Parameters Demo
int add(int a, int b) {
    return a + b;
}

int multiply(int a, int b) {
    return a * b;
}

void functionDemo() {
    printf("=== Function Demo ===\n");
    
    int x = 10, y = 5;
    
    printf("Addition: %d + %d = %d\n", x, y, add(x, y));
    printf("Multiplication: %d * %d = %d\n", x, y, multiply(x, y));
    
    printf("\n");
}

// 6. Recursion Demo
int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

void recursionDemo() {
    printf("=== Recursion Demo ===\n");
    
    int n = 5;
    printf("Factorial of %d: %d\n", n, factorial(n));
    
    printf("Fibonacci sequence up to %d: ", n);
    for (int i = 0; i < n; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n\n");
}

// 7. Structure Demo
struct Student {
    char name[50];
    int age;
    float gpa;
};

void structureDemo() {
    printf("=== Structure Demo ===\n");
    
    struct Student student1;
    strcpy(student1.name, "John Doe");
    student1.age = 20;
    student1.gpa = 3.8;
    
    printf("Student Name: %s\n", student1.name);
    printf("Student Age: %d\n", student1.age);
    printf("Student GPA: %.2f\n", student1.gpa);
    
    printf("\n");
}

// 8. Dynamic Memory Allocation Demo
void dynamicMemoryDemo() {
    printf("=== Dynamic Memory Allocation Demo ===\n");
    
    int n = 5;
    int *dynamicArray = (int*)malloc(n * sizeof(int));
    
    if (dynamicArray == NULL) {
        printf("Memory allocation failed!\n");
        return;
    }
    
    // Initialize array
    for (int i = 0; i < n; i++) {
        dynamicArray[i] = (i + 1) * 10;
    }
    
    printf("Dynamic array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", dynamicArray[i]);
    }
    printf("\n");
    
    // Resize array
    dynamicArray = (int*)realloc(dynamicArray, (n + 2) * sizeof(int));
    dynamicArray[n] = 60;
    dynamicArray[n + 1] = 70;
    
    printf("Resized array: ");
    for (int i = 0; i < n + 2; i++) {
        printf("%d ", dynamicArray[i]);
    }
    printf("\n");
    
    free(dynamicArray);
    printf("Memory freed successfully!\n\n");
}

// 9. File Operations Demo
void fileOperationsDemo() {
    printf("=== File Operations Demo ===\n");
    
    FILE *file;
    char filename[] = "demo.txt";
    char content[] = "Hello, World!\nThis is a demo file.\n";
    char buffer[100];
    
    // Write to file
    file = fopen(filename, "w");
    if (file != NULL) {
        fprintf(file, "%s", content);
        fclose(file);
        printf("File written successfully!\n");
    } else {
        printf("Error opening file for writing!\n");
        return;
    }
    
    // Read from file
    file = fopen(filename, "r");
    if (file != NULL) {
        printf("File content:\n");
        while (fgets(buffer, sizeof(buffer), file) != NULL) {
            printf("%s", buffer);
        }
        fclose(file);
    } else {
        printf("Error opening file for reading!\n");
    }
    
    printf("\n");
}

// 10. Mathematical Operations Demo
void mathematicalOperationsDemo() {
    printf("=== Mathematical Operations Demo ===\n");
    
    double num1 = 16.0;
    double num2 = 3.0;
    
    printf("Square root of %.1f: %.2f\n", num1, sqrt(num1));
    printf("Power: %.1f^%.1f = %.2f\n", num2, 2.0, pow(num2, 2.0));
    printf("Ceiling of %.1f: %.0f\n", num2, ceil(num2));
    printf("Floor of %.1f: %.0f\n", num2, floor(num2));
    printf("Absolute value of -%.1f: %.1f\n", num2, fabs(-num2));
    printf("Natural log of %.1f: %.2f\n", num1, log(num1));
    printf("Sine of %.1f: %.2f\n", num2, sin(num2));
    printf("Cosine of %.1f: %.2f\n", num2, cos(num2));
    
    printf("\n");
}

// 11. Sorting Algorithm Demo (Bubble Sort)
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap elements
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void sortingDemo() {
    printf("=== Sorting Demo (Bubble Sort) ===\n");
    
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printf("Original array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    bubbleSort(arr, n);
    
    printf("Sorted array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n\n");
}

// 12. Binary Search Demo
int binarySearch(int arr[], int left, int right, int target) {
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        }
        
        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;
}

void searchDemo() {
    printf("=== Binary Search Demo ===\n");
    
    int arr[] = {2, 3, 4, 10, 40, 50, 60, 70, 80, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 40;
    
    printf("Array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    int result = binarySearch(arr, 0, n - 1, target);
    
    if (result == -1) {
        printf("Element %d not found in array\n", target);
    } else {
        printf("Element %d found at index %d\n", target, result);
    }
    
    printf("\n");
}

// 13. Linked List Demo
struct Node {
    int data;
    struct Node* next;
};

void insertNode(struct Node** head, int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = *head;
    *head = newNode;
}

void printList(struct Node* head) {
    while (head != NULL) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

void linkedListDemo() {
    printf("=== Linked List Demo ===\n");
    
    struct Node* head = NULL;
    
    insertNode(&head, 3);
    insertNode(&head, 2);
    insertNode(&head, 1);
    
    printf("Linked list: ");
    printList(head);
    
    printf("\n");
}

// 14. Stack Implementation Demo
#define MAX_SIZE 100

struct Stack {
    int items[MAX_SIZE];
    int top;
};

void initStack(struct Stack* s) {
    s->top = -1;
}

int isEmpty(struct Stack* s) {
    return s->top == -1;
}

int isFull(struct Stack* s) {
    return s->top == MAX_SIZE - 1;
}

void push(struct Stack* s, int item) {
    if (isFull(s)) {
        printf("Stack overflow!\n");
        return;
    }
    s->items[++s->top] = item;
}

int pop(struct Stack* s) {
    if (isEmpty(s)) {
        printf("Stack underflow!\n");
        return -1;
    }
    return s->items[s->top--];
}

void stackDemo() {
    printf("=== Stack Implementation Demo ===\n");
    
    struct Stack stack;
    initStack(&stack);
    
    push(&stack, 10);
    push(&stack, 20);
    push(&stack, 30);
    
    printf("Popped: %d\n", pop(&stack));
    printf("Popped: %d\n", pop(&stack));
    printf("Popped: %d\n", pop(&stack));
    
    printf("\n");
}

// Main function to run all demos
int main() {
    printf("=== C Programming Demo Codes Collection ===\n\n");
    
    dataTypesDemo();
    arrayOperationsDemo();
    stringManipulationDemo();
    pointerOperationsDemo();
    functionDemo();
    recursionDemo();
    structureDemo();
    dynamicMemoryDemo();
    fileOperationsDemo();
    mathematicalOperationsDemo();
    sortingDemo();
    searchDemo();
    linkedListDemo();
    stackDemo();
    
    printf("=== All demos completed successfully! ===\n");
    
    return 0;
}
