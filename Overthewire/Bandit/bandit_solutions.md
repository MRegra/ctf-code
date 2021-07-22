# Solutions of Overthewire Bandit Challenges

## Level: bandit0 -> bandit1

**Main URL:** https://overthewire.org/wargames/bandit/bandit0.html and https://overthewire.org/wargames/bandit/bandit1.html

**Writeup:**  
This is a fairly easy challenge. To solve this one simply has to read a little the ssh manual.
We know that the user is bandit0, the address is bandit.labs.overthewire.org and that the port is 2220.
Once we combine this into an ssh command we get:

    ssh bandit0@bandit.labs.overthewire.org -p 2220 

After pressing enter, we are asked if we want to continue connecting, after typing yes we have to put a password, and in this case, by reading the challenge description we know that it is bandit0.

And we are in!

To get the flag, we have to simply see the contents of the file readme by running the command cat readme, which returns:

**Flag:** boJ9jbbUNNfktd78OOpsqOltutMc3MY1

____________________________________


## Level: bandit1 -> bandit2

**Main URL:** https://overthewire.org/wargames/bandit/bandit2.html

**Writeup:**  
First we have to use the same command as in the previous challenge, but this time the user is bandit1 and the password is the flag of the previous challenge. The ssh command is:

    ssh bandit1@bandit.labs.overthewire.org -p 2220 

After putting the flag from the previous challenge as the password we are in!

To get the flag, we have to simply see the contents of the file - 

To see the contents of - we cannot simply run cat - this will result in a endless wait, and the command do not return anything.

To see the contents we have to indicate the path, in this case:

    cat ./-

Meaning that we want to cat the file with the name - in the present directory.

And the flag is:

**Flag:** CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

____________________________________


## Level: bandit2 -> bandit3

**Main URL:** https://overthewire.org/wargames/bandit/bandit3.html

**Writeup:**  
As in the previous one we have to use the same command as in the previous challenge, but this time the user is bandit2 and the password is the flag of the previous challenge. The ssh command is:

    ssh bandit2@bandit.labs.overthewire.org -p 2220 

After putting the flag from the previous challenge as the password we are in!

To get the flag, we have to simply see the contents of the file "spaces in this filename" 

To see the contents of spaces in this filename we have to be carefull with the spaces. But this is also simple, one simply has to use the back lash everytime there is a space ;)

To see the contents we have to indicate the path, in this case:

    cat spaces\ in\ this\ filename

And the flag is:

**Flag:** UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

____________________________________


## Level: bandit3 -> bandit4

**Main URL:** https://overthewire.org/wargames/bandit/bandit4.html

**Writeup:**  
As in the previous one we have to use the same command as in the previous challenge, but this time the user is bandit2 and the password is the flag of the previous challenge. The ssh command is:

    ssh bandit2@bandit.labs.overthewire.org -p 2220 

After putting the flag from the previous challenge as the password we are in!

To get the flag, we have to simply see the contents of the hidden file in the folder inhere.

To be able to find hidden files using the Linux terminal we have to use a flag of the command ls, in particular the -a flag, which, according to the ls manual: 

    -a, --all
        do not ignore entries starting with .

Knowing this, what we have to do is simply to go inside the inhere forlder, by usind the cd command like such:

    cd inhere

And once inside we have to list all files, without ignoring the ones that start with . which in Linux are the hidden files.

    ls -a

And we are presented with: .  ..  .hidden

The first . is the current directory, the two points, .. is the previous directory and the .hidden is the file we want!!

Now to see the contents you know the drill:

    cat .hidden

And the flag is:

**Flag:** pIwrPrtPN36QITSp3EQaw936yaFoFgAB

____________________________________


## Level: bandit4 -> bandit5

**Main URL:** https://overthewire.org/wargames/bandit/bandit5.html

**Writeup:**  
As in the previous one we have to use the same command as in the previous challenge, but this time the user is bandit2 and the password is the flag of the previous challenge. The ssh command is:

    ssh bandit2@bandit.labs.overthewire.org -p 2220 

After putting the flag from the previous challenge as the password we are in!

In this one we have to find the file that is human readable, so ASCII, or something like that.
After entering the machine we can see the home directory contents by using the ls command, we are presented with just one folder, inhere, after moving inside it, by using cd inhere, we can see the inhere directory contents once again with ls.

This time, we get the following:

    bandit4@bandit:~/inhere$ ls 
    -file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09

We can go one by one but it takes time! We can, instead, leverage the linux terminal tools that we have at our disposal, in particular the file command, that, according to its manual:

    NAME
        file — determine file type
        
What we can do is to simply see the file type for all the files inside the inhere directory by using the command:

    bandit4@bandit:~/inhere$ file ./*
    ./-file00: data
    ./-file01: data
    ./-file02: data
    ./-file03: data
    ./-file04: data
    ./-file05: data
    ./-file06: data
    ./-file07: ASCII text
    ./-file08: data
    ./-file09: data

So it seems that the file ./-file07 has the flag because it is the only one with ASCII text, which is human readable. Lets cat its contents to see!

    bandit4@bandit:~/inhere$ cat ./-file07

And the flag is:

**Flag:** koReBOKuIDDepwhWk7jZC0RTdopnAYKh

____________________________________
