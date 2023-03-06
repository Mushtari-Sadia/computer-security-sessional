# computer-security-sessional

## assignment on cryptography
The purpose of this assignment is to implement a hybrid cryptosystem using both symmetric and asymmetric cryptography mechanisms. We used AES as the symmetric algorithm and RSA as the asymmetric cryptography algorithm.


## assignment on buffer overflow
Buffer overflow is defined as the condition in which a program attempts to write data beyond the boundaries of pre-allocated fixed length buffers. This vulnerability can be utilized by a malicious user to alter the flow control of the program, even execute arbitrary pieces of code. This vulnerability arises due to the mixing of the storage for data (e.g. buffers) and the storage for controls (e.g. return addresses): an overflow in the data part can affect the control flow of the program, because an overflow can change the return address.

In this assignment, we were given a program that has the buffer-overflow problem, and we needed to exploit the vulnerability to gain the root privilege. Moreover, we had to experiment with several protection schemes that have been implemented in Linux, and evaluate their effectiveness.

## assignment on web security

- **CSRF**:
The objective of this lab is to help us understand the Cross-Site Request Forgery (CSRF) attack. A CSRF attack involves a victim user, a trusted site, and a malicious site. The victim user holds an active session with a trusted site while visiting a malicious site. The malicious site injects an HTTP request for the trusted site into the victim user session, causing damages.
In this lab, we attacked a social networking web application using the CSRF attack. The open-source social networking application is called Elgg, which has already been installed in our VM.
Elgg has countermeasures against CSRF, but we have turned them off for the purpose of this lab. This lab covers the following topics:

        • Cross-Site Request Forgery attack

        • CSRF countermeasures: Secret token and Same-site cookie

        • HTTP GET and POST requests

        • JavaScript and Ajax

- **XSS**:
Cross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications. This vulnerability makes it possible for attackers to inject malicious code (e.g. JavaScripts) into victim's web browser.
To demonstrate what attackers can do, a web application named Elgg is set up in a pre-built Ubuntu VM image.Some of Elgg's protection methods are commented out, intentionally making it vulnerable to XSS attacks. We needed to exploit the vulnerabilities to launch attacks in a way that is similar to what Samy Kamkar did to MySpace in 2005 through the notorious Samy worm. The ultimate goal of this attack is to spread an XSS worm among the users, such that whoever views an infected user profile will be infected, and whoever is infected will add you (i.e., the attacker) to his/her friend list.

- **SQL Injection**:
SQL injection is a code injection technique that exploits the vulnerabilities in the interface between web applications and database servers. The vulnerability is present when user's inputs are not correctly checked within the web applications before being sent to the back-end database servers. Many web applications take inputs from users, and then use these inputs to construct SQL queries, so the web applications can get information from the database. Web applications also use SQL queries to store information in the database. These are common practices in the development of web applications. When SQL queries are not carefully constructed, SQL injection vulnerabilities can occur. The SQL injection attack is one of the most common attacks on web applications.
In this lab, web application is created that is vulnerable to the SQL injection attack. Our web application includes the common mistakes made by many web developers. Our goal is to find ways to exploit the SQL injection vulnerabilities, demonstrate the damage that can be achieved by the attack, and master the techniques that can help defend against such type of attacks.


## assignment on security tool

In this assignment, we had to deliver the following elements on an existing security tool 'androRAT'

    Instructions for Presentation (Deliverable 1)
    - General overview of the tool(s)
    - Purpose and high-level features of the tool(s)
    - Background Information
    - Technical design and working principles of the tool(s)
    - Demonstration of the tool(s) most useful features (Can be shown with screenshots)
    - For case study topics, present some example scenarios where the tools could have been used or real-life scenarios where they have already been used.
    - Limitations of the tool(s)

    Instruction for Demonstration Video (Deliverable 2)
    - Demonstrate major features of the tool(s)
    - Try to provide short theoretical explanations on how the features have been implemented
    - Mention (or demonstrate if applicable) the limitations of the tools
    - Mention the challenges you encountered while setting up the environment and using the tool(s)
    - For case study topics, discuss the tools in depth.




## assignment on malware

The Morris worm (November 1988) was one of the oldest computer worms distributed via the Internet, and
the frst to gain signifcant mainstream media attention. While it is old, the techniques used by most
worms today are still the same, such as the WannaCry ransomware in 2017. They involve two main parts:
attack and self-duplication. The attack part exploits a vulnerability (or a few of them), so a worm can get
entry to another computer. The self-duplication part is to send a copy of itself to the compromised machine,
and then launch the attack from there. A detailed analysis of the Morris worm was given by Spafford.

The goal of this assignment is to help you gain a better understanding of the behavior of worms, by
writing a simple worm and testing it in a contained environment (an Internet emulator). Although this
assignment focuses on Morris worm, the underneath technique used is quite generic. We have broken down
the assignment into several tasks, so that you can build the worm incrementally.
For testing, we built two emulated Internets, a small one and a larger one. You can release your worms
in each of these Internets, and see how the worms spread across the entire emulated Internet.

## assignment on firewall

The learning objective of this lab is two-fold: learning how firewalls work, and setting up a simple firewall
for a network. Students will first implement a simple stateless packet-filtering firewall, which inspects packets, and decides whether to drop or forward a packet based on firewall rules. Through this implementation
task, students can get the basic ideas on how firewall works.
Actually, Linux already has a built-in firewall, also based on netfilter. This firewall is called
iptables. Students will be given a simple network topology, and are asked to use iptables to set up
firewall rules to protect the network. Students will also be exposed to several other interesting applications
of iptables. This lab covers the following topics:

        • Firewall
        • Netfilter
        • Loadable kernel module
        • Using iptables to set up firewall rules
        • Various applications of iptables