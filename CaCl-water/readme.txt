WHAM simulation is performed to get the PMF.
equil contains files that can equilibrate the starting configuration. After running the files in equil using gromacs, 
copy equil*.gro to umbrella.

umbrella contains files that does the wham simulation. run sub.pbs first. after that run copy_umb.sh. then run the following command:

gmx wham -it tpr-files.dat -ix pullx-files.dat -o -hist -unit kT
