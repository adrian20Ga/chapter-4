<h1>Chapter 4</h1>

***

<h2>Files</h2>

files is important when it comes to accessing it, we can access it with special commands for input and output.
With this we can access the file and modify it as the user wishes.
in each programming language it allows in the handling of files but the most used is the c language.

```tcc
//this pointer is used to communicate the program to the file
FILE *fptr;
```
***


```tcc
//this is the syntax to open a file
ptr = fopen("fileopen","mode");
```

***

```tcc
// this will close the file with a pointer
fclose(fptr);
```

## Type of file
- <h2>Binary</h2> of this type is the least used due to its difficulty in interpreting it and its extension is .txt
- <h2>text</h2> this is the most used and the most understandable to handle and its extension is .bin

 <h2>Mode</h2>
To manipulate the files we have to use parameters that are the following

- b:        open a file in format binary.
- W:        open a file to write.
- r:        open a file to read.
- a:        open a file append.
- fscanf()	Read an input of the file.
- fprintf()	Write the output on the file.

strings
- fgets()	Read a string of the file
- fputs()	Write a string on the file

***

***

<h1>Arrays</h1>

arrays are variables that can store values ​​for example minecraft boxes, understanding this topic at first sounds difficult but with practice it becomes simple and can even become your best ally, and it is storage by the memory volatil, for arrays they will always start at 0,1,2,3 ...

<h3>types of arrays</h3>


***


- Array
```tcc
//below we init the variable array
int gupy[6] = {1, 10, 8, 17, 9,4,3};
```

- Array of arrays
```tcc
//this is a 2d array
int gupy[2][3] = {{1, 5, 0}, {-1, 5, 9}};
```  


```tcc
// a 3d array
int gupy[2][3][4] = {{{3, 4, 2, 3}, {0, -3, 9, 11}, {23, 12, 23, 2}}, {{13, 4, 56, 3}, {5, 9, 3, 5}, {3, 1, 4, 9}}};
```








.
