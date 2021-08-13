# Solutions of Overthewire Bandit Challenges

_______________________________________

## Hello!! Welcome to my Github Overthewire Bandit writeups. Please, checkout my blog: 
# https://mregraoncyber.com/category/overthewire/bandit/ 
## In my blog you have these solutions and a lot more! Hope you enjoy!
_______________________________________

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
As in the previous one we have to use the same command as in the previous challenge, but this time the user is bandit3 and the password is the flag of the previous challenge. The ssh command is:

    ssh bandit3@bandit.labs.overthewire.org -p 2220

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
As in the previous one we have to use the same command as in the previous challenge, but this time the user is bandit4 and the password is the flag of the previous challenge. The ssh command is:

    ssh bandit4@bandit.labs.overthewire.org -p 2220

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

## Level: bandit5 -> bandit6

**Main URL:** https://overthewire.org/wargames/bandit/bandit6.html

**Writeup:**
As in the previous one we have to use the same command as in the previous challenge, but this time the user is bandit5 and the password is the flag of the previous challenge. The ssh command is:

    ssh bandit5@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have to find the file that is human readable, so ASCII, or something like that, that has 1033 bytes in size and that is not executable.
After entering the machine we can see the home directory contents by using the ls command, we are presented with just one folder, inhere, after moving inside it, by using cd inhere, we can see the inhere directory contents once again with ls.

This time, we get the following:

    bandit5@bandit:~/inhere$ ls
    maybehere00  maybehere03  maybehere06  maybehere09  maybehere12  maybehere15  maybehere18
    maybehere01  maybehere04  maybehere07  maybehere10  maybehere13  maybehere16  maybehere19
    maybehere02  maybehere05  maybehere08  maybehere11  maybehere14  maybehere17

We can go one directory at a time and then analyze the contents of each directory but that takes alot time! We can, instead, leverage the linux terminal tools that we have at our disposal, in particular the file and find commands.

What we can do is to simply see the file is of the type ASCII, and, if so, if the size is 1033 bytes, and if so, if it is not executable. The final command:

    bandit5@bandit:~/inhere$ file ./* | grep "ASCII" | find . -type f -size 1033c ! -executable
    ./maybehere07/.file2

So it seems that the file ./maybehere07/.file2 has the flag because it is the only one, now, what is left to do is simply to cat its contets, as such:

    bandit5@bandit:~/inhere$ cat ./maybehere07/.file2

And the flag is:

**Flag:** DXjZPULLxYr17uwoI01bNLQbtFemEgo7

____________________________________

## Level: bandit6 -> bandit7

**Main URL:** https://overthewire.org/wargames/bandit/bandit7.html

**Writeup:**
As in the previous one we have to use the same command as in the previous challenge, but this time the user is bandit6 and the password is the flag of the previous challenge. The ssh command is:

    ssh bandit6@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have to find the file that is owned by user bandit7, owned by group bandit6 and with 33 bytes in size.
After entering the machine we can see the home directory contents by using the ls command, we are presented with nothin, there is no directory or interesting file in the home directory.

We can analyze the contents of the entire machine but that takes alot time! We can, instead, leverage the linux terminal tools that we have at our disposal, in particular the find command.

We can simply use a combination of commands, as such:

    bandit6@bandit:~/ find /* -type f -group bandit6 -user bandit7 -size 33c 2>/dev/null
    /var/lib/dpkg/info/bandit7.password

So it seems that the file ./maybehere07/.file2 has the flag because it is the only one, now, what is left to do is simply to cat its contets, as such:

    bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password

And the flag is:

**Flag:** HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

____________________________________

## Level: bandit7 -> bandit8

**Main URL:** https://overthewire.org/wargames/bandit/bandit8.html

**Writeup:**
As in the previous one we have to use the same command as in the previous challenge, but this time the user is bandit7 and the password is the flag of the previous challenge. The ssh command is:

    ssh bandit7@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have to find the word millionth in the file data.txt.
After entering the machine we can see the home directory contents by using the ls command, we are presented with the file data.txt.

This challenge turned out to be quite simple, I simply did:

    bandit7@bandit:~$ cat data.txt | grep millionth

And the flag is:

**Flag:** cvX2JJa4CFALtqS87jk27qwqGhBM9plV

____________________________________

## Level: bandit8 -> bandit9

**Main URL:** https://overthewire.org/wargames/bandit/bandit9.html

**Writeup:**
As in the previous one we have to use the same command as in the previous challenge, but this time the user is bandit8 and the password is the flag of the previous challenge. The ssh command is:

    ssh bandit8@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "The password for the next level is stored in the file data.txt and is the only line of text that occurs only once"

A funny challenge I got to say! Well, after some online search I found that if you use the uniq command you can count the number of ocorrences of a line in a file. However, if it is not sorted it will not work. So first, we must sort the file and pipe the content into the uniq command with the -u flag (-u flag for unique occurrence), as such:

    bandit8@bandit:~$ sort data.txt | uniq -u

And the flag is:

**Flag:** UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

____________________________________

## Level: bandit9 -> bandit10

**Main URL:** https://overthewire.org/wargames/bandit/bandit10.html

**Writeup:**
As in the previous one we have to use the same command as in the previous challenge, but this time the user is bandit9 and the password is the flag of the previous challenge. The ssh command is:

    ssh bandit9@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters."

Weird challenge! Well, after some online search I found that if you use the strings command with on the file and then piped the output int the grep with two equal signs we would get the flag. The final command:

    bandit9@bandit:~$ strings data.txt | grep ==

And the flag is:

**Flag:** truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

____________________________________

## Level: bandit10 -> bandit11

**Main URL:** https://overthewire.org/wargames/bandit/bandit11.html

**Writeup:**
As in the previous one we have to use the same command as in the previous challenge, but this time the user is bandit10 and the password is the flag of the previous challenge. The ssh command is:

    ssh bandit10@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "The password for the next level is stored in the file data.txt, which contains base64 encoded data"

In this one we have yet again the data.txt file. Inside it we can see a base64 string. We know it is base64 because it ends with two equal signs (which is common for base 64 enconding).
To decode it and get the flag, we can cat the contents of the file and piped them into the command base64 --decode, as such:

    bandit10@bandit:~$ cat data.txt | base64 --decode

And the flag is:

**Flag:** IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

____________________________________

## Level: bandit11 -> bandit12

**Main URL:** https://overthewire.org/wargames/bandit/bandit12.html

**Writeup:**
As in the previous one we have to use the same command as in the previous challenge, but this time the user is bandit11 and the password is the flag of the previous challenge. The ssh command is:

    ssh bandit11@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions"

In this one we have yet again the data.txt file. Inside it we can see a weird string. We know it is rotated by 13 positions. This is a form of "encryption" known as ROT13. After googling for a while I found the regex combination that allows me to reverse this. The final command I used was:

    bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'

And the flag is:

**Flag:** 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

____________________________________

## Level: bandit12 -> bandit13

**Main URL:** https://overthewire.org/wargames/bandit/bandit13.html

**Writeup:**
As in the previous one we have to use the same command as in the previous challenge, but this time the user is bandit12 and the password is the flag of the previous challenge. The ssh command is:

    ssh bandit12@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed."

This was a different challenge. First time I worked with compreesed files this way, and with different compressed programs, well a funny way overall.
For starters I did as suggested and created a "working directory" under /tmp by running the command:

    bandit12@bandit:~$ mkdir /tmp/working_dir

Then I copied the data.txt file, that is in the home directory, into this new directory I just created by running the command:

    bandit12@bandit:~$ cp data.txt /tmp/working_dir

And finaly I moved to that file:

    bandit12@bandit:~$ cd /tmp/working_dir

Now we have everything to start cracking!
First we have to get the file from the hexdump, we know from the description that data.txt is the hexdump of a file... To get the file we can run the command:

    bandit12@bandit:/tmp/working_dir$ xxd -r data.txt data

Now we have a file called data. Now we need to figure out the correct compression used, to do so, we simply have to run the command:

    bandit12@bandit:/tmp/working_dir$ file data
    data: gzip compressed data, was "data2.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix

And then:

    bandit12@bandit:/tmp/working_dir$ mv data data.gz && gzip -dk data.gz && ls
    data  data.gz  data.txt

We have a new data file!! Let's see the file type of this one:

    bandit12@bandit:/tmp/working_dir$ file data
    data: bzip2 compressed data, block size = 900k

So this time is bzip2, after searching online I discovered that the extension is bz2 and to open it we can do:

    bandit12@bandit:/tmp/working_dir$ mv data data.bz2 && bzip2 -dk data.bz2 && ls
    data  data.bz2  data.gz  data.txt

And now we have to repeate the process...

    bandit12@bandit:/tmp/working_dir$ mv data data.gz && gzip -dk data.gz && ls
    data  data.bz2  data.gz  data.txt

A new data file poped out:

    bandit12@bandit:/tmp/working_dir$ file data
    data: POSIX tar archive (GNU)

This time is a POSIX tar archive (GNU), after searching online I was able to dicover that the extension is tar.gz and to open it:

    bandit12@bandit:/tmp/working_dir$ mv data data.tar.gz && tar -xvf data.tar.gz && ls
    data5.bin
    data5.bin  data.bz2  data.gz  data.tar.gz  data.txt

We now have a data5.bin!!

    bandit12@bandit:/tmp/working_dir$ file data5.bin
    data5.bin: POSIX tar archive (GNU)

Next step...

    bandit12@bandit:/tmp/working_dir$ mv data5.bin data.tar.gz && tar -xvf data.tar.gz && ls
    data6.bin
    data6.bin  data.bz2  data.gz  data.tar.gz  data.txt

Next we have:

    bandit12@bandit:/tmp/working_dir$ file data6.bin
    data6.bin: bzip2 compressed data, block size = 900k

Next we have:

    bandit12@bandit:/tmp/working_dir$ mv data6.bin data.bz2 && bzip2 -dk data.bz2 && ls
    data  data.bz2  data.gz  data.tar.gz  data.txt

Next:

    bandit12@bandit:/tmp/working_dir$ file data
    data: POSIX tar archive (GNU)

Next:

    bandit12@bandit:/tmp/working_dir$ mv data data.tar.gz && tar -xvf data.tar.gz && ls
    data8.bin
    data8.bin  data.bz2  data.gz  data.tar.gz  data.txt

Next:

    bandit12@bandit:/tmp/working_dir$ file data8.bin
    data8.bin: gzip compressed data, was "data9.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix

Next:

    bandit12@bandit:/tmp/working_dir$ mv data8.bin data.gz && gzip -dk data.gz && ls
    data  data.bz2  data.gz  data.tar.gz  data.txt

Next:

    bandit12@bandit:/tmp/working_dir$ file data
    data: ASCII text
    bandit12@bandit:/tmp/working_dir$ cat data
    The password is ***************************

And the flag is:

**Flag:** 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

____________________________________

## Level: bandit13 -> bandit14

**Main URL:** https://overthewire.org/wargames/bandit/bandit14.html

**Writeup:**
As in the previous one we have to use the same command as in the previous challenge, but this time the user is bandit11 and the password is the flag of the previous challenge. The ssh command is:

    ssh bandit13@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level."

Ok this is a interesting one. It looks like it is different from the rest. No password, instead a private SSH key? In the home directory after listing the contents I found a file: sshkey.private
I decided to cat its contents and I saw a private key. This is what we need to access the next level!!

I copied its contents to a file on my machine. Well to make sure this is correct and that this is the way to access the next level I had to try. To do so I searched online for a while. I searched for "How to access ssh with private key" and I found a few links with useful information. And in the end I decided to try this set of commands:

First I need to give full writing and reading permissions to the file where I stored the private key, as such:

    mregra on Cyber:~$ chmod 600 sshkey.private

Now we can run the ssh command:

    mregra on Cyber:~$ ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220

Note: You need to be in the folder where sshkey.private is stored, otherwise you may need to provide the full path.

And with this we got access to the next level!!

The flag to the level is:

**Flag:** 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

____________________________________

## Level: bandit14 -> bandit15

**Main URL:** https://overthewire.org/wargames/bandit/bandit15.html

**Writeup:**
The access to this challenge was done in the previous challenge, take a look above.

In this one we have the following description:

    "The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost."

To discover the protocol running on that port and which other port was open I ran the command:

    bandit14@bandit:~$ nmap 127.0.0.1
    Starting Nmap 7.40 ( https://nmap.org ) at 2021-08-13 09:09 CEST
    Nmap scan report for localhost (127.0.0.1)
    Host is up (0.00034s latency).
    Not shown: 998 closed ports
    PORT      STATE SERVICE
    22/tcp    open  ssh
    30000/tcp open  ndmps

    Nmap done: 1 IP address (1 host up) scanned in 0.08 seconds

Ok se we have a port running the service ndmps over tcp. I decided to try to use netcat to get the flag, as such:

    bandit14@bandit:~$ nc localhost 30000

After this I simply clicked enter and got this error:

    Wrong! Please enter the correct current password

Ok now we know we have to insert the password for this level, that according to the previous one is on the file /etc/bandit_pass/bandit14. I tried again and got the flag.

    bandit14@bandit:~$ nc localhost 30000
    4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e                  <- This is the flag for the current level
    Correct!
    BfMYroe26WYalil77FoDi9qh59eK5xNr


And the flag is:

**Flag:** BfMYroe26WYalil77FoDi9qh59eK5xNr

____________________________________
