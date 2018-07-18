# Hasher
Hashes specific files or file system trees
Hasher.py requires the -p flag in order to hash the tree of a specific file path.

The -o option provides the ability to rename the default Hashes.pkl output file where the hashes are stored.

The -c option compares the hashes of a previous output file to the hashes of a given file path and its tree. Additionally, to use the -c option you must run the program once to generate an output file and then use -c to compare. 

****Notice****
for the -c option
	Hasher_v1.py does not detect if a file has been moved to a different directory
	Hasher_v1.py does not detect if all the data in a file has been removed resulting in no hash when comparing hash to file
