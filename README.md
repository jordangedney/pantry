Pantry
======
A recipe suggestion app, currently being developed for web 




======
Programming Rules
======
1. Rule of Modularity: Write simple parts connected by clean interfaces. 
2. Rule of Clarity: Clarity is better than cleverness. 
3. Rule of Composition: Design programs to be connected to other programs. 
4. Rule of Separation: Separate policy from mechanism; separate interfaces from engines. 
5. Rule of Simplicity: Design for simplicity; add complexity only where you must. 
6. Rule of Parsimony: Write a big program only when it is clear by demonstration that nothing else will do. 
7. Rule of Transparency: Design for visibility to make inspection and debugging easier. 
8. Rule of Robustness: Robustness is the child of transparency and simplicity. 
9. Rule of Representation: Fold knowledge into data so program logic can be stupid and robust. 
10. Rule of Least Surprise: In interface design, always do the least surprising thing.
11. Rule of Silence: When a program has nothing surprising to say, it should say nothing.
12. Rule of Repair: When you must fail, fail noisily and as soon as possible.
13. Rule of Economy: Programmer time is expensive; conserve it in preference to machine time. 
14. Rule of Generation: Avoid hand-hacking; write programs to write programs when you can. 
15. Rule of Optimization: Prototype before polishing. Get it working before you optimize it.
16. Rule of Diversity: Distrust all claims for “one true way”.
17. Rule of Extensibility: Design for the future, because it will be here sooner than you think.
======
Database Guidelines
======
I was looking for some tips for you guys and found these.
They will probably make more sense once you jump in but i'm saving them here

1)Keep different types of data separate - don't store addresses in your order table, 
link to an address in a separate addresses table, for example.

2)I personally like having an integer or long surrogate key on each table 
(that holds data, not those that link different tables together, e,g., m:n relationships) that is the primary key.

3)I also like having a created and modified timestamp column.

4)Ensure that every column that you do "where column = val" in any query has an index. 
Maybe not the most perfect index in the world for the data type, but at least an index.

5)Set up your foreign keys. Also set up ON DELETE and ON MODIFY rules where relevant, 
to either cascade or set null, depending on your object structure 
(so you only need to delete once at the 'head' of your object tree, 
and all that object's sub-objects get removed automatically).

