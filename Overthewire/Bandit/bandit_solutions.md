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

    bandit5@bandit:~/inhere$ find . -type f -size 1033c ! -executable
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

This was a different challenge. First time I worked with compressed files this way, and with different compressed programs, well a funny way overall.
For starters I did as suggested and created a "working directory" under /tmp by running the command:

    bandit12@bandit:~$ mkdir /tmp/working_dir

Then I copied the data.txt file, that is in the home directory, into this new directory I just created by running the command:

    bandit12@bandit:~$ cp data.txt /tmp/working_dir

And finally I moved to that file:

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
As in the previous one we have to use the same command as in the previous challenge, but this time the user is bandit13 and the password is the flag of the previous challenge. The ssh command is:

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

## Level: bandit15 -> bandit16

**Main URL:** https://overthewire.org/wargames/bandit/bandit16.html

**Writeup:**
As in the previous challenges we have to use the same command:

    ssh bandit15@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.

    Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…"

Ok this is a interesting one. We have to connect using SSL encryption. Well, after some search I found that nmap as a command which is ncat that allows us to specify the encryption protocol as ssl, the host and the port, as such:

    bandit15@bandit:~$ ncat --ssl 127.0.0.1 30001

Afterwards I simply inserted the level's password and got the following:

    bandit15@bandit:~$ ncat --ssl 127.0.0.1 30001
    BfMYroe26WYalil77FoDi9qh59eK5xNr                  <- This is the flag for the current level
    Correct!
    cluFn7wTiGryunymYOu4RcffSxQluehd

The flag to the level is:

**Flag:** cluFn7wTiGryunymYOu4RcffSxQluehd

____________________________________


## Level: bandit16 -> bandit17

**Main URL:** https://overthewire.org/wargames/bandit/bandit17.html

**Writeup:**
As in the previous challenges we have to use the same command:

    ssh bandit16@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it."

Ok this is a interesting one. We first need to find all open ports between 31000 and 32000, to do so I used nmap as such:

    bandit16@bandit:~$ nmap -p 31000-32000 127.0.0.1

    Starting Nmap 7.40 ( https://nmap.org ) at 2021-08-18 11:43 CEST
    Nmap scan report for localhost (127.0.0.1)
    Host is up (0.00022s latency).
    Not shown: 996 closed ports
    PORT      STATE SERVICE
    31046/tcp open  unknown
    31518/tcp open  unknown
    31691/tcp open  unknown
    31790/tcp open  unknown
    31960/tcp open  unknown

    Nmap done: 1 IP address (1 host up) scanned in 0.09 seconds
    bandit16@bandit:~$

It seems that ports 31046, 31518, 31691, 31790 and 31960 are open, now we need to know which of those speak SSL. To know if they speak SSL I used the openssl command.

    bandit16@bandit:~$ openssl s_client -connect 127.0.0.1:port         <- Use each port to test.

Some of the ports did not allowed me to put some input, so I excluded those, however, 2 of them did allow input, the port 31518 and the port 31790. After trying both I got an SSH private key.

The flag to the level is an SSH private key.

____________________________________


## Level: bandit17 -> bandit18

**Main URL:** https://overthewire.org/wargames/bandit/bandit18.html

**Writeup:**
To access this challenge I used a different command than the previous one, first this time we have to use a private key, not a password. In order to use the private key (that w found in the previous challenge) we need to give the file certain permissions, as such:


    mregra on Cyber:~$ chmod 600 sshkey.private

Now we can run the ssh command:

    mregra on Cyber:~$ ssh -i sshkey.private bandit17@bandit.labs.overthewire.org -p 2220

And we are in!!

In this one we have the following description:

    "There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

    NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19"

This challenged turned out to be quite simple.
What I did was simply run the diff command as such:

    bandit17@bandit:~$ diff passwords.old passwords.new
    42c42
    < w0Yfolrc5bwjS4qw5mq1nnQi6mF03bii
    ---
    > kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
    bandit17@bandit:~$

The flag to the level is:

**Flag:** kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd

____________________________________


## Level: bandit18 -> bandit19

**Main URL:** https://overthewire.org/wargames/bandit/bandit19.html

**Writeup:**
As in the previous challenges we have to use the same command:

    ssh bandit18@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in... Oh wait! No we got a:

    Byebye !
    Connection to bandit.labs.overthewire.org closed.

Let's analyze the challenge description, it might help. In this one we have the following description:

    "The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH."

Ok, so we now know that we will automatically get logged out, but we can run commands on the machine using ssh, I first tried the following:

    mregra on Cyber:~$ ssh bandit18@bandit.labs.overthewire.org -p 2220 ls
    This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

    bandit18@bandit.labs.overthewire.org's password:
    readme
    mregra on Cyber:~$

We have a file readme in the home directory. We can try to cat its contents, according to the description, the flag is inside! So I simply ran the command:

    mregra on Cyber:~$ ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
    This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

    bandit18@bandit.labs.overthewire.org's password:
    IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
    mregra on Cyber:~$

The flag to the level is:

**Flag:** IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x

____________________________________


## Level: bandit19 -> bandit20

**Main URL:** https://overthewire.org/wargames/bandit/bandit20.html

**Writeup:**
As in the previous challenges we have to use the same command:

    ssh bandit19@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary."

After some time I noticed that the bandit20-do executable is running commands as bandit20.
To read the password for bandit19 what I did was simply cat the contents of /etc/bandit_pass/bandit20 with the executable, as such:

    bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
    GbKksEFF4yrVs6il55v6gwY5aVje5f0j

The flag to the level is:

**Flag:** GbKksEFF4yrVs6il55v6gwY5aVje5f0j

____________________________________


## Level: bandit20 -> bandit21

**Main URL:** https://overthewire.org/wargames/bandit/bandit21.html

**Writeup:**
As in the previous challenges we have to use the same command:

    ssh bandit20@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

    NOTE: Try connecting to your own network daemon to see if it works as you think"

We have executable that connects to a running server, and once it receives from the server the password for the present level, checks if it is correct and if so, returns the password for the next level.
It makes sense and it seems simple. What we have to do is simply to create a netcat server running on localhost in a port of our choice. To do so I ran the following command:

    bandit20@bandit:~$ nc -l -p 4444

Then I went to another terminal, create another ssh connection to the machine and I used the executable on the port 4444, as such:

    bandit20@bandit:~$ ./suconnect 4444

Then I simply went back to the server I created and I entered the password for the present level, and this was the result:

In the server terminal:

    bandit20@bandit:~$ nc -l -p 4444
    GbKksEFF4yrVs6il55v6gwY5aVje5f0j
    gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
    bandit20@bandit:~$

In the executable terminal:

    bandit20@bandit:~$ ./suconnect 4444
    Read: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
    Password matches, sending next password
    bandit20@bandit:~$

The flag to the level is:

**Flag:** gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

____________________________________


## Level: bandit21 -> bandit22

**Main URL:** https://overthewire.org/wargames/bandit/bandit22.html

**Writeup:**
As in the previous challenges we have to use the same command:

    ssh bandit21@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed."

Cron, what is that? I've never heard about it before. I did some research and I was able to find that "cron job is a time-based job scheduler in Unix-like computer operating systems".

Interesting software, I might even start using if myself! Now, for the writeup, according to the description we should take a look at /etc/cron.d/ and I did so:

    bandit21@bandit:/$ cd /etc/cron.d
    bandit21@bandit:/etc/cron.d$ ls
    cronjob_bandit15_root  cronjob_bandit22  cronjob_bandit24
    cronjob_bandit17_root  cronjob_bandit23  cronjob_bandit25_root
    bandit21@bandit:/etc/cron.d$ cat cronjob_bandit22
    @reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
    * * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
    bandit21@bandit:/etc/cron.d$

We want bandit22, because that is the next level. I decided to cat the contents of cronjob_bandit22. Interesting, there is one job at /usr/bin/cronjob_bandit22.sh
I decided to try to cat its contents:

    bandit21@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit22.sh
    #!/bin/bash
    chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
    cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
    bandit21@bandit:/etc/cron.d$

Aperently, the flag from bandit22 is inserted into /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv. As you know, the cat command prints to the stdout whatever is inside the file, and the > sign indicates that the output from the cat command is inserted into the file /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv. I decided to cat its contents and got the flag.

The flag to the level is:

**Flag:** Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

____________________________________


## Level: bandit22 -> bandit23

**Main URL:** https://overthewire.org/wargames/bandit/bandit23.html

**Writeup:**
As in the previous challenges we have to use the same command:

    ssh bandit22@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

    NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints."

Once again, we have cron. They suggest us once again to look inside /etc/cron.d like we did in the previous challenge:

    bandit22@bandit:~$ cd /etc/cron.d
    bandit22@bandit:/etc/cron.d$ ls
    cronjob_bandit15_root  cronjob_bandit22  cronjob_bandit24
    cronjob_bandit17_root  cronjob_bandit23  cronjob_bandit25_root
    bandit22@bandit:/etc/cron.d$ cat cronjob_bandit23
    @reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
    * * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null

We have a cron job for bandit23. Let's analyze the script:

    bandit22@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit23.sh
    #!/bin/bash

    myname=$(whoami)
    mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

    echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

    cat /etc/bandit_pass/$myname > /tmp/$mytarget

It is a relatilvely simple script to read. The first command whoami returns the name of the user running the script, in this case bandit23. The second command, converts into md5sum the output from the echo command and removes the space and the - left by the md5sum.
Finally it cats the password for the user into /tmp/$mytarget and we know that mytarget is the md5sum done before.
I decided to copy to my machine the first part of the script, and change it a little, as such:

    #!/bin/bash

    myname="bandit23"
    mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
    echo $mytarget

The output of this was: 8ca319486bfbbc3663ea0fbe81326349
I went back to the bandit22@bandit machine and ran the command:

    bandit22@bandit:/etc/cron.d$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349

And I got the flag.

The flag to the level is:

**Flag:** jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n

____________________________________


## Level: bandit23 -> bandit24

**Main URL:** https://overthewire.org/wargames/bandit/bandit24.html

**Writeup:**
As in the previous challenges we have to use the same command:

    ssh bandit23@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

    NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

    NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…"

Once again, we have cron. They suggest us once again to look inside /etc/cron.d like we did in the previous challenge:

    bandit23@bandit:~$ cd /etc/cron.d
    bandit23@bandit:/etc/cron.d$ ls
    cronjob_bandit15_root  cronjob_bandit22  cronjob_bandit24
    cronjob_bandit17_root  cronjob_bandit23  cronjob_bandit25_root
    bandit23@bandit:/etc/cron.d$ cat cronjob_bandit24
    @reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
    * * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null

Like in the previous one, let's analyze the contents of /usr/bin/cronjob_bandit24.sh:

    bandit23@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit24.sh
    #!/bin/bash

    myname=$(whoami)

    cd /var/spool/$myname
    echo "Executing and deleting all scripts in /var/spool/$myname:"
    for i in * .*;
    do
        if [ "$i" != "." -a "$i" != ".." ];
        then
            echo "Handling $i"
            owner="$(stat --format "%U" ./$i)"
            if [ "${owner}" = "bandit23" ]; then
                timeout -s 9 60 ./$i
            fi
            rm -f ./$i
        fi
    done

    bandit23@bandit:/etc/cron.d$

By reading the code, it is clear that the script above is running the scripts in /var/spool/bandit24 before deleting them. I decided to take advantage of this and create a script:

    #!/bin/bash

    cat /etc/bandit_pass/bandit24 > /tmp/bandit24_flag/flag_bandit24

I did the follwoing:

    nano script.sh

Then I pasted the script above on script.sh openend with nano. Afterwards, I gave the file execution permissions by running the command:

    chmod 777 script.sh

That gave execution permissions to everyone. Then I created the folder and file on tmp, as such:

    cd /tmp && mkdir bandit24_flag && touch flag_bandit24 && chmod 666 flag_bandit24

This command creates the directory, creates the file and gives everyone permissions to write in the file.

Finally I went to the folder /tmp/bandit24_flag and there it was the flag!

The flag to the level is:

**Flag:** UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

____________________________________


## Level: bandit24 -> bandit25

**Main URL:** https://overthewire.org/wargames/bandit/bandit25.html

**Writeup:**
As in the previous challenges we have to use the same command:

    ssh bandit24@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing."

Well I decided to create a script to brute-force the password, here it is:

    #!/bin/bash

    echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0000"
    for i in {1..10000}
    do
            value=$( printf '%04d' $i )
            echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ" $value
    done

The flag to the level is:

**Flag:** uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

____________________________________


## Level: bandit25 -> bandit26

**Main URL:** https://overthewire.org/wargames/bandit/bandit26.html

**Writeup:**
As in the previous challenges we have to use the same command:

    ssh bandit25@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it."

This challenge was weird. I was not succeding on cracking this! I search on goolge more and more, and I fiannly decided to get a little help! I was able to find on my own the bandit26 shell, in particular:

First what I did was to enter on bandit25 to checkout what was given to me. There I found a sshkey for bandit26. After getting the key I tried to access the challenge but it was in fact not possible, the connection was automatically close.
Apparently this is due to the fact that the bash is "not /bin/bash, but something else". I then decided to look for a file from bandit26, by running the command:

    cat /etc/passwd | grep bandit26

I decided to use the /etc/passwd file because, according to Wikipédia:

    "The /etc/passwd file is a text-based database of information about users that may log into the system or other operating system user identities that own running processes."

And the output from the command above was the following:

    bandit25@bandit:~$ cat /etc/passwd | grep bandit26
    bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext

Now lets analyze the contents of showtext:

    bandit25@bandit:~$ cat /usr/bin/showtext
    #!/bin/sh

    export TERM=linux

    more ~/text.txt
    exit 0
    bandit25@bandit:~$

Ok, so, we know that it calls the function more from the bash, we may exploit that, by repeating the ssh command to access bandit26 but in a smaller window, triggering the more function:

    ssh -i sshkey.private bandit26@bandit.labs.overthewire.org -p 2220

Then, if in a small window we should be presented with the more function, instead of scrolling down, we can insert commands. To do so, type v to be able to inject commands.
Afterwards, we can now setup the correct shell, by running the command:

    :set shell=/bin/bash

Then, we just need to call shell, as such

    :shell

And we should be prompted with the bash!! We can now simply cat the password:

    :shell
    bandit26@bandit:~$ cat /etc/bandit_pass/bandit26

The flag to the level is:

**Flag:** 5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z

____________________________________


## Level: bandit26 -> bandit27

**Main URL:** https://overthewire.org/wargames/bandit/bandit27.html

**Writeup:**

In this one we have the following description:

    "Good job getting a shell! Now hurry and grab the password for bandit27!"

Well, using the same technique as before we can access the bandit26 shell.
Once in the shell I did ls to list the contents of the home directory:

    :shell
    bandit26@bandit:~$ ls
    bandit27-do  text.txt

We have an interesting file, the "bandit27-do"
I tried to run it:

    bandit26@bandit:~$ ./bandit27-do
    Run a command as another user.
        Example: ./bandit27-do id

Ok, this is similar to a previous one, so I simply tried the command:

    bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27

The flag to the level is:

**Flag:** 3ba3118a22e93127a4ed485be72ef5ea

____________________________________


## Level: bandit27 -> bandit28

**Main URL:** https://overthewire.org/wargames/bandit/bandit28.html

**Writeup:**
As in the previous challenges we have to use the same command:

    ssh bandit2@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "There is a git repository at ssh://bandit27-git@localhost/home/bandit27-git/repo. The password for the user bandit27-git is the same as for the user bandit27.

    Clone the repository and find the password for the next level."

For this one we apparently need to clone a git repository.
I am familiered with git, I use it regularly daily. The thing is, inside Bandit machine we cannot create folders inside the home folder.
Therefore I remembered from previous challenges that we have write and create permissions on the /tmp directory.
Knowing this I did the following:

    bandit27@bandit:~$ mkdir /tmp && cd /tmp/
    bandit27@bandit:/tmp$ mkdir git && cd git/
    bandit27@bandit:/tmp/git$ git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
    Cloning into 'repo'...
    Could not create directory '/home/bandit27/.ssh'.
    The authenticity of host 'localhost (127.0.0.1)' can't be established.
    ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
    Are you sure you want to continue connecting (yes/no)? yes
    Failed to add the host to the list of known hosts (/home/bandit27/.ssh/known_hosts).
    This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

    bandit27-git@localhost's password:
    remote: Counting objects: 3, done.
    remote: Compressing objects: 100% (2/2), done.
    remote: Total 3 (delta 0), reused 0 (delta 0)
    Receiving objects: 100% (3/3), done.

Now we have the repo in the bandit machine, we now can look at its contents:

    bandit27@bandit:/tmp/git$ ls
    repo
    bandit27@bandit:/tmp/git$ cd repo/
    bandit27@bandit:/tmp/git/repo$
    bandit27@bandit:/tmp/git/repo$ ls
    README
    bandit27@bandit:/tmp/git/repo$ cat README
    The password to the next level is: ********************************

The flag to the level is:

**Flag:** 0ef186ac70e04ea33b4c1853d2526fa2

____________________________________


## Level: bandit28 -> bandit29

**Main URL:** https://overthewire.org/wargames/bandit/bandit29.html

**Writeup:**
As in the previous challenges we have to use the same command:

    ssh bandit28@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo. The password for the user bandit28-git is the same as for the user bandit28.

    Clone the repository and find the password for the next level."

Well, it is the same as the previous one?!
I started the same way:

    bandit28@bandit:~$ cd /tmp/
    bandit28@bandit:/tmp$ mkdir bandit28-git
    bandit28@bandit:/tmp$ cd bandit28-git
    bandit28@bandit:/tmp/bandit28-git$
    bandit28@bandit:/tmp/bandit28-git$ git clone ssh://bandit28-git@localhost/home/bandit28-git/repo
    Cloning into 'repo'...
    Could not create directory '/home/bandit28/.ssh'.
    The authenticity of host 'localhost (127.0.0.1)' can't be established.
    ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
    Are you sure you want to continue connecting (yes/no)? yes
    Failed to add the host to the list of known hosts (/home/bandit28/.ssh/known_hosts).
    This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

    bandit28-git@localhost's password:
    remote: Counting objects: 9, done.
    remote: Compressing objects: 100% (6/6), done.
    remote: Total 9 (delta 2), reused 0 (delta 0)
    Receiving objects: 100% (9/9), done.
    Resolving deltas: 100% (2/2), done.
    bandit28@bandit:/tmp/bandit28-git$
    bandit28@bandit:/tmp/bandit28-git$ ls
    repo
    bandit28@bandit:/tmp/bandit28-git$ cd repo/
    bandit28@bandit:/tmp/bandit28-git/repo$
    bandit28@bandit:/tmp/bandit28-git/repo$ ls
    README.md

Now lets look at the README.md contents:

    bandit28@bandit:/tmp/bandit28-git/repo$ cat README.md
    # Bandit Notes
    Some notes for level29 of bandit.

    ## credentials

    - username: bandit29
    - password: xxxxxxxxxx

We have no flag here... Maybe they commited it before by mistake? I know that happens (not to me of course! cof cof)
To see the previous commits I usually use the Github website. Now we'll need to use the git bash as such:

    bandit28@bandit:/tmp/bandit28-git/repo$ git log
    commit edd935d60906b33f0619605abd1689808ccdd5ee
    Author: Morla Porla <morla@overthewire.org>
    Date:   Thu May 7 20:14:49 2020 +0200

    fix info leak

    commit c086d11a00c0648d095d04c089786efef5e01264
    Author: Morla Porla <morla@overthewire.org>
    Date:   Thu May 7 20:14:49 2020 +0200

    add missing data

    commit de2ebe2d5fd1598cd547f4d56247e053be3fdc38
    Author: Ben Dover <noone@overthewire.org>
    Date:   Thu May 7 20:14:49 2020 +0200

    initial commit of README.md
    bandit28@bandit:/tmp/bandit28-git/repo$

We had an info leak!! Nice! Maybe this is it? To check I ran the following command:

    bandit28@bandit:/tmp/bandit28-git/repo$ git diff edd935d60906b33f0619605abd1689808ccdd5ee c086d11a00c0648d095d04c089786efef5e01264
    diff --git a/README.md b/README.md
    index 5c6457b..3f7cee8 100644
    --- a/README.md
    +++ b/README.md
    @@ -4,5 +4,5 @@ Some notes for level29 of bandit.
    ## credentials

    - username: bandit29
    -- password: xxxxxxxxxx
    +- password: ********************************

    bandit28@bandit:/tmp/bandit28-git/repo$

The flag to the level is:

**Flag:** bbc96594b4e001778eee9975372716b2

____________________________________


## Level: bandit29 -> bandit30

**Main URL:** https://overthewire.org/wargames/bandit/bandit30.html

**Writeup:**
As in the previous challenges we have to use the same command:

    ssh bandit29@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "There is a git repository at ssh://bandit29-git@localhost/home/bandit29-git/repo. The password for the user bandit29-git is the same as for the user bandit29.

    Clone the repository and find the password for the next level."

In this one I started like in the previous ones by cloning the git repo to /tmp/bandit29-git/
After that was finished I listed the contents of the repo and I noticed that only a README.md was there:

    bandit29@bandit:/tmp/bandit29_git/repo$ ls
    README.md

I decided to checkout its contents:

    bandit29@bandit:/tmp/bandit29_git/repo$ cat README.md 
    # Bandit Notes
    Some notes for bandit30 of bandit.

    ## credentials

    - username: bandit30
    - password: <no passwords in production!>

Ok, we have a lead! "<no passwords in production>", does this mean that there are other branches, like develop branches? Let's list all the existing remote branches and see:

    bandit29@bandit:/tmp/bandit29_git/repo$ git branch -r
    origin/HEAD -> origin/master
    origin/dev
    origin/master
    origin/sploits-dev

Nice! We have a dev branch! Let's pull its contents:

    bandit29@bandit:/tmp/bandit29_git/repo$ git checkout origin/dev
    Note: checking out 'origin/dev'.

    You are in 'detached HEAD' state. You can look around, make experimental
    changes and commit them, and you can discard any commits you make in this
    state without impacting any branches by performing another checkout.

    If you want to create a new branch to retain commits you create, you may
    do so (now or later) by using -b with the checkout command again. Example:

    git checkout -b <new-branch-name>

    HEAD is now at bc83328... add data needed for development
    bandit29@bandit:/tmp/bandit29_git/repo$ ls
    code  README.md
    bandit29@bandit:/tmp/bandit29_git/repo$ cat README.md 
    # Bandit Notes
    Some notes for bandit30 of bandit.

    ## credentials

    - username: bandit30
    - password: ********************************

The flag to the level is:

**Flag:** 5b90576bedb2cc04c86a9e924ce42faf

____________________________________


## Level: bandit30 -> bandit31

**Main URL:** https://overthewire.org/wargames/bandit/bandit31.html

**Writeup:**
As in the previous challenges we have to use the same command:

    ssh bandit30@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "There is a git repository at ssh://bandit30-git@localhost/home/bandit30-git/repo. The password for the user bandit30-git is the same as for the user bandit30.

    Clone the repository and find the password for the next level."

In this challenge I started as in the previous one, and first I cloned the git repo into /tmp/bandit30-git/
Afterwards I listed the contents of the repo folder and noticed that there was only a README.md file:

    bandit30@bandit:/tmp/bandit30-git/repo$ ls
    README.md
    bandit30@bandit:/tmp/bandit30-git/repo$ cat README.md 
    just an epmty file... muahaha

Ok, so nothing inside the README.md that can be useful.
I decided to check the branches:

    bandit30@bandit:/tmp/bandit30-git/repo$ git branch -r
    origin/HEAD -> origin/master
    origin/master

Just one, the master, nothing useful. Than I checked the log:

    bandit30@bandit:/tmp/bandit30-git/repo$ git log
    commit 3aefa229469b7ba1cc08203e5d8fa299354c496b
    Author: Ben Dover <noone@overthewire.org>
    Date:   Thu May 7 20:14:54 2020 +0200

        initial commit of README.md
    bandit30@bandit:/tmp/bandit30-git/repo$

Just one commit. Nothing here too. I thought for a while and I browsed the .git folder and on the file packed-refs I found something interesting!

    bandit30@bandit:/tmp/bandit30-git/repo/.git$ cat packed-refs 
    # pack-refs with: peeled fully-peeled 
    3aefa229469b7ba1cc08203e5d8fa299354c496b refs/remotes/origin/master
    f17132340e8ee6c159e0a4a6bc6f80e1da3b1aea refs/tags/secret

There seems to exist a secret tag!! Lets see:

    bandit30@bandit:/tmp/bandit30-git/repo$ git tag
    secret

Indeed! Now lets show it:

    bandit30@bandit:/tmp/bandit30-git/repo$ git show secret
    ********************************

The flag to the level is:

**Flag:** 47e603bb428404d265f59c42920d81e5

____________________________________


## Level: bandit31 -> bandit32

**Main URL:** https://overthewire.org/wargames/bandit/bandit32.html

**Writeup:**
As in the previous challenges we have to use the same command:

    ssh bandit31@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo. The password for the user bandit31-git is the same as for the user bandit31.

    Clone the repository and find the password for the next level."

Similarly to the previous challenge, in this challenge I started by first cloning the git repo into /tmp/bandit31-git/
Afterwards I listed the contents of the repo folder and noticed that there was only a README.md file:

    bandit31@bandit:/tmp/bandit31-git/repo$ ls
    README.md
    bandit31@bandit:/tmp/bandit31-git/repo$ cat README.md 
    This time your task is to push a file to the remote repository.

    Details:
        File name: key.txt
        Content: 'May I come in?'
        Branch: master

Ok, we need to create a file named key.txt, with the contents 'May I come in?' and commit it to the master branch.
Let's first create the file, I decided to use the text editor Vim, you can use nano for example if you want.

    bandit31@bandit:/tmp/bandit31-git/repo$ vim key.txt

And then I pasted the contents: May I come in? (without the quotes).

Now that we have the file created, we need to commit it to git, to do so, first we need to add the file, them commit it and finally push it to the master branch, as such:

    bandit31@bandit:/tmp/bandit31-git/repo$ git add key.txt -f

The -f is necessary, to bypass the gitignore folder that apparently is blocking the key.txt file, this way we can commit it anyway.

    bandit31@bandit:/tmp/bandit31-git/repo$ git commit -m "Bandit31 solution by MRegra"
    [master 5e89a96] Bandit31 solution by MRegra
    1 file changed, 1 insertion(+), 1 deletion(-)
    bandit31@bandit:/tmp/bandit31-git/repo$ git push
    Could not create directory '/home/bandit31/.ssh'.
    The authenticity of host 'localhost (127.0.0.1)' can't be established.
    ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
    Are you sure you want to continue connecting (yes/no)? yes
    Failed to add the host to the list of known hosts (/home/bandit31/.ssh/known_hosts).
    This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

    bandit31-git@localhost's password: 
    Counting objects: 6, done.
    Delta compression using up to 2 threads.
    Compressing objects: 100% (4/4), done.
    Writing objects: 100% (6/6), 560 bytes | 0 bytes/s, done.
    Total 6 (delta 1), reused 0 (delta 0)
    remote: ### Attempting to validate files... ####
    remote: 
    remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
    remote: 
    remote: Well done! Here is the password for the next level:
    remote: ********************************
    remote: 
    remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
    remote:        

I did not specify the branch because we are on the master branch already (you can check by running the command git branch -r).
If you want to specify the branch this would be a way to do it:

    git push origin master

The flag to the level is:

**Flag:** 56a9bf19c63d650ce78e6ec0354ee45e

____________________________________


## Level: bandit32 -> bandit33

**Main URL:** https://overthewire.org/wargames/bandit/bandit33.html

**Writeup:**
As in the previous challenges we have to use the same command:

    ssh bandit32@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "After all this git stuff its time for another escape. Good luck!"

This was a weird one. After inserting the password we are presented with this:

    WELCOME TO THE UPPERCASE SHELL
    >> 

An uppercase shell, I did a few tests:

    WELCOME TO THE UPPERCASE SHELL
    >> ls
    sh: 1: LS: not found
    >> cd
    sh: 1: CD: not found
    >> CD
    sh: 1: CD: not found
    >> LS
    sh: 1: LS: not found
    >> 

It is converting all the inserted commands into uppercase. I searched online for a way to exit this weird shell and go to the normal one, and I found out that we can actually use $0, as such:

    >> $0
    $ ls
    uppershell
    $ 

Why you may ask? Well, so did I! After some research I was able to find out a prety good explanation. 

    mregra@pop-os:~/hacking$ echo 'echo $0' > random_script.sh
    mregra@pop-os:~/hacking$ sh random_script.sh 
    random_script.sh
    mregra@pop-os:~/hacking$ chmod +x random_script.sh 
    mregra@pop-os:~/hacking$ ./random_script.sh 
    ./random_script.sh
    mregra@pop-os:~/hacking$ 

As you can see, the $0 is the first actual argument of sh, in our case random_script.sh. The same thing happens even when we execute the script as an executable.

In the Bandit challenge case, the uppercase is a binary executable that is calling:
    
    sh -c "some_input_from_the_user"

We know this because of the error messages:

    sh: 1: CD: not found

If you test on your own machine: sh -c 'echo $0', as we did before, you will get sh! Therefore, you are on a shell, and if you run sh -c $0 you'll get a terminal:

    mregra@pop-os:~/hacking$ sh -c 'echo $0'
    sh
    mregra@pop-os:~/hacking$ sh -c $0
    mregra@pop-os:~/hacking$ 

And on the bandit machine challenge:

    >> $0
    $ 

Ok, we now have the shell!! I decided to list the contents of the home directory:

    $ ls -al
    total 28
    drwxr-xr-x  2 root     root     4096 May  7  2020 .
    drwxr-xr-x 41 root     root     4096 May  7  2020 ..
    -rw-r--r--  1 root     root      220 May 15  2017 .bash_logout
    -rw-r--r--  1 root     root     3526 May 15  2017 .bashrc
    -rw-r--r--  1 root     root      675 May 15  2017 .profile
    -rwsr-x---  1 bandit33 bandit32 7556 May  7  2020 uppershell
    $ 

Ok, we have just the uppershell scrip. Let's see if we can simply cat the password to the next level from the bandit33 file (like with did in other challenges):

    $ cat /etc/bandit_pass/bandit33
    ********************************
    $ 


The flag to the level is:

**Flag:** c9c3199ddf4121b10cf581a98d51caee

____________________________________


## Level: bandit33 -> bandit34

**Main URL:** https://overthewire.org/wargames/bandit/bandit34.html

**Writeup:**
As in the previous challenges we have to use the same command:

    ssh bandit33@bandit.labs.overthewire.org -p 2220

After putting the flag from the previous challenge as the password we are in!

In this one we have the following description:

    "At this moment, level 34 does not exist yet."

After entering the challenge I did as usual:

    bandit33@bandit:~$ ls
    README.txt
    bandit33@bandit:~$ cat README.txt 
    Congratulations on solving the last level of this game!

    At this moment, there are no more levels to play in this game.  However, we are constantly working
    on new levels and will most likely expand this game with more levels soon.
    Keep an eye out for an announcement on our usual communication  channels!
    In the meantime, you could play some of our other wargames.

    If you have an idea for an awesome new level, please let us know!
    bandit33@bandit:~$ 

I guess it is all done! :D
____________________________________

