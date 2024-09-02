# piet-modern
Quick projects to be interpreted by the npiet interpreter. Exploring piet invariants and writing quick scripts to allow for easier editing, alternate color schemes

# To do
## Editor setup
I would like to be able to edit in a text/csv editor using 1A - 6C for the 6 shades and colors, plus W and B for white and black.
This will be converted to the npiet format, .ppm using python. 

Combined with a color palette file .json using key-value pairs to decode each letter, can convert to a .ppm with a more modern color scheme.

Done! Next is refactoring the code so that we can keep color palettes in a separate json file.

##Invariants: It would be cool to demonstrate piet invariants, perhaps using piet itself? Interesting idea. 

To demonstrate: store something in the stack (hello world? Just Hi?), perform the invariant until identity, the output the stack, repeat.

Even better! Use the invariants as a series of programs that look different but accomplish the same thing. Maybe. If you can be clever about it I think you can have fun.

## Linux issue
For some reason, the python code to read the ppm output using the python Pillow package fails on my Linux Mint install.
