# Searching for designs using the GAP system
This section explains how one can use the code found in ``gap_functions.g`` to search 
through character tables in the GAP system. It requires a working installation of GAP
which can be found at https://www.gap-system.org/Download/. GAP also comes preinstalled 
with sage found at https://doc.sagemath.org/html/en/installation/index.html.

To use the functions one first reads the file:
````GAP
gap> Read("PATH_TO_FOLDER/gap_functions.g");
````
Assuming this is done, one can find unitary 2-designs using the function ``DesignsFromGroup``. 
The function takes a group name as an argument and searches the irreducible characters 
of it's representations to check if the squared norm of a character equals 2. 
It returns a record containing the size of the group and the dimensions where a 
unitary 2-design was found. As an example we find designs from the group "2.U4(2)" below.
````GAP
gap> DesignsFromGroup("2.U4(2)");
rec( dim := rec( 4 := [ 21, 22 ], 5 := [ 2, 3 ] ), size := 51840 )
````
The output shows that the group contains unitary 2-designs in dimensions 4 and 5. The
lists contain the numbers of the irreducible characters corresponding to the unitary
2-designs. Below we show how one can confirm that character number 21 indeed gives
a unitary 2-design in dimension 4.
````GAP
gap> t := Irr(CharacterTable("2.U4(2)"));;
gap> chr := t[21];;
gap> Norm(chr * chr);
2
gap> Degree(chr);
4
````
To get designs from a list of group names, one can use either the function
``GroupDesigns`` or the function `DesignsByDim`. The first returns a record with names
of groups as indexes. These then contain records similar to the ones from
``DesignsFromGroup``. The second function returns a record indexing first by the
dimension where unitary 2-designs were found and then by the size of the group.
We explain using the following example.
````GAP
gap> groups := ["6.A7", "2.U4(2)", "L3(2)"];;
gap> DesignsByDim(groups);
rec( 3 := rec( 168 := rec( ("L3(2)") := [ 2, 3 ] ) ), 
     4 := rec( 15120 := rec( ("6.A7") := [ 10, 11 ] ), 51840 := rec( ("2.U4(2)") := [ 21, 22 ] ) ), 
     5 := rec( 51840 := rec( ("2.U4(2)") := [ 2, 3 ] ) ), 
     6 := rec( 15120 := rec( ("6.A7") := [ 31, 32, 33, 34 ] ) ) )
````
Here one sees that for the groups `"6.A7"`, `"2.U4(2)"`and  `"L3(2)"` there are unitary 
2-designs in dimensions 3, 4, 5 and 6. For dimension 4 there are representations of
sizes 15120 and 51840. The ones of size 15120 come from the group "6.A7" and have
irreducible character numbers 10 and 11.

# Excluding non-Clifford designs based Sylow's 3rd theorem
The file `sylow_exclusions.py` contains a function `one_sylow` which can exclude
non-Clifford orders for designs. To check if an order is excluded one simply runs the
command:
````commandline
python PATH_TO_FOLDER/sylow_exclusions.py order
````
For the script to work one needs to have a list of all primes smaller than or equal
to the order saved as a file ``primes.npy``. One can get this by running the command:
````commandline
python PATH_TO_FOLDER/generate_primes.py order
````
