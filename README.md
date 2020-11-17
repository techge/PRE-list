PRE-list
========

List of (automatic) protocol reverse engineering tools/methods/approaches for network protocols

# Overview

NetT: input is a network trace (e.g. pcap)<br />
ExeT: input is an execution trace (code/binary at hand)<br />
PF: output is protocol format (describing the syntax)<br />
PFSM: output is protocol finite state machine (describing semantic/sequential logic)<br />

| Name | Year | NetT | ExeT | PF | PFSM |
|------|------|------|------|----|------|
| AFL [[1]](#1) | 2014 |  | x |  |  | 
| ARGOS [[2]](#2) | 2015 |  | x |  |  | 
| ARTISTE [[3]](#3) | 2012 |  | x |  |  | 
| ASAP [[4]](#4) | 2011 | x |  |  |  | 
| Antunes and Neves [[5]](#5) | 2009 | x |  |  | x | 
| AutoFormat [[6]](#6) | 2008 |  | x | x |  | 
| AutoReEngine [[7]](#7) | 2013 | x |  | x | x | 
| Biprominer [[8]](#8) | 2011 | x |  | x | x | 
| Boosting [[9]](#9) | 2008 | x |  |  |  | 
| Cai et al. [[10]](#10) | 2016 | x |  | x |  | 
| ConfigRE [[11]](#11) | 2008 |  | x |  |  | 
| Discoverer [[12]](#12) | 2007 | x |  | x |  | 
| Dispatcher [[13]](#13) | 2009 |  | x |  |  | 
| Dispatcher2 [[14]](#14) | 2013 |  | x |  |  | 
| FFE/x86 [[15]](#15) | 2006 |  | x |  |  | 
| FieldHunter [[16]](#16) | 2015 | x |  |  |  | 
| Fuzzgrind [[17]](#17) | 2009 |  | x |  |  | 
| GAPA [[18]](#18) | 2005 |  | x | x | x | 
| Goo et al. [[19]](#19) | 2019 | x |  | x | x | 
| Howard [[20]](#20) | 2011 |  | x |  |  | 
| IPART [[21]](#21) | 2020 | x |  | x |  | 
| Laroche et al. [[22]](#22) | 2013 | x |  |  | x | 
| MACE [[23]](#23) | 2010 |  | x |  |  | 
| Ma et al. [[24]](#24) | 2006 | x |  |  |  | 
| Meng et al. [[25]](#25) | 2014 | x |  |  | x | 
| Netzob [[26]](#26) | 2012 | x | x | x | x | 
| PEXT [[27]](#27) | 2007 |  | x |  | x | 
| PIP [[28]](#28) | 2004 | x |  |  |  | 
| PRISMA [[29]](#29) | 2012 | x |  |  |  | 
| PULSAR [[30]](#30) | 2015 |  |  |  |  | 
| Polyglot [[31]](#31) | 2007 |  | x | x |  | 
| PowerShell [[32]](#32) | 2017 | x |  |  |  | 
| ProDecoder [[33]](#33) | 2012 | x |  | x |  | 
| ProGraph [[34]](#34) | 2015 | x |  | x |  | 
| ProHacker [[35]](#35) | 2017 | x |  |  |  | 
| ProPrint [[36]](#36) | 2017 | x |  |  |  | 
| ProVeX [[37]](#37) | 2013 | x |  |  |  | 
| Prospex [[38]](#38) | 2009 | x |  | x |  | 
| REWARDS [[39]](#39) | 2010 |  | x |  |  | 
| RS Cluster [[40]](#40) | 2015 | x |  |  |  | 
| ReFormat [[41]](#41) | 2009 |  | x | x |  | 
| Replayer [[42]](#42) | 2006 |  | x |  |  | 
| ReverX [[43]](#43) | 2011 | x |  |  | x | 
| RolePlayer [[44]](#44) | 2006 | x |  |  |  | 
| Rosetta [[45]](#45) | 2007 |  | x |  |  | 
| ScriptGen [[46]](#46) | 2005 | x |  |  |  | 
| Shim et al. [[47]](#47) | 2020 | x |  | x |  | 
| Sun et al. [[48]](#48) | 2020 |  |  |  |  | 
| Trifilo et al. [[49]](#49) | 2009 | x |  |  | x | 
| Tupni [[50]](#50) | 2008 |  | x | x |  | 
| UPCSS [[51]](#51) | 2015 | x |  |  |  | 
| Veritas [[52]](#52) | 2011 | x |  |  | x | 
| WASp [[53]](#53) | 2016 | x |  | x |  | 
| Wang et al. [[54]](#54) | 2013 | x |  | x |  | 
| Xiao et al. [[55]](#55) | 2009 |  | x |  | x | 
| Yang et al. [[56]](#56) | 2020 | x |  | x |  | 
| Zhang et al. [[57]](#57) | 2012 | x |  |  | x | 

# References

#### [1]
Zalewski, M.: American Fuzzy Loop. http://lcamtuf.coredump.cx/afl/technical_details.txt
#### [2]
Zeng, J., Lin, Z.: Towards automatic inference of kernel object semantics from binary code. In: 18th International Symposium, RAID 2015, vol. 9404, pp. 538–561. Springer, Kyoto (2015). doi:10.1007/978-3-319-26362-5
#### [3]
Caballero, J., Grieco, G., Marron, M., Lin, Z., Urbina, D.: ARTISTE: Automatic Generation of Hybrid Data Structure Signatures from Binary Code Executions. Technical Report TR-IMDEA-SW-2012-001, IMDEA Software Institute, Madrid (2012)
#### [4]
T. Krueger, N. Krmer, and K. Rieck, “Asap: automatic semantics-aware analysis of network payloads,” in Proceedings of the ECML/PKDD, 2011. [PDF](https://oar.tib.eu/jspui/bitstream/123456789/2288/1/664831966.pdf)
#### [5]
J. Antunes and N. Neves, “Building an automaton towards reverse protocol engineering,” 2009, http://www.di.fc.ul.pt/∼nuno/PAPERS/INFORUM09.pdf.
#### [6]
Z. Lin, X. Jiang, D. Xu, and X. Zhang, “Automatic protocol format reverse engineering through context-aware monitored execution,” in Proceedings of the 15th Symposium on Network and  Distributed System Security (NDSS ’08), February 2008.
#### [7]
J.-Z. Luo and S.-Z. Yu, “Position-based automatic reverse engineering of network protocols,” Journal of Network and Computer Applications, vol. 36, no. 3, pp. 1070–1077, 2013.
#### [8]
Y. Wang, X. Li, J. Meng, Y. Zhao, Z. Zhang, and L. Guo, “Biprominer: automatic mining of binary protocol features,” in Proceedings of the 12th International Conference on Parallel and Distributed Computing, Applications and Technologies (PDCAT ’11), pp. 179–184, October 2011.
#### [9]
K. Gopalratnam, S. Basu, J. Dunagan, and H. J. Wang, “Automatically extracting fields from unknown network protocols,” in Proceedings of the 15th Symposium on Network and Distributed System Security (NDSS ’08), 2008. [PDF](http://www.nicemice.net/helen/papers/sysml-Gopalratnam.pdf)
#### [10]
J. Cai, J. Luo, and F. Lei, “Analyzing network protocols of application layer using hidden Semi-Markov model,” Mathematical Problems in Engineering, vol. 2016, Article ID 9161723, 14 pages, 2016.
#### [11]
Wang, R., Wang, X., Zhang, K., Li, Z.: Towards automatic reverse engineering of software security configurations. In: Proceedings of the 15th ACM Conference on Computer and Communications Security, CCS ’08, pp. 245–256. ACM, Limerick (2008). doi:10.1145/1455770.1455802
#### [12]
W. Cui, J. Kannan, and H. J. Wang, “Discoverer: automatic protocol description generation from network traces,” in Proceedings of the USENIX Security Symposium, 2007. 
#### [13]
J. Caballero, P. Poosankam, C. Kreibich, and D. Song, “Dispatcher: enabling active botnet infiltration using automatic protocol reverse-engineering,” in Proceedings of the 16th ACM Conference on Computer and Communications Security (CCS ’09), pp. 621–634, ACM, Chicago, Ill, USA, November 2009. [PDF](https://people.eecs.berkeley.edu/~dawnsong/papers/2009%20Dispatcher.pdf)
#### [14]
J. Caballero and D. Song, “Automatic protocol reverse-engineering: message format extraction and field semantics inference,” Computer Networks, vol. 57, no. 2, pp. 451–474, 2013. [PDF](http://www.academia.edu/download/47267446/j.comnet.2012.08.00320160715-7025-1uns1ji.pdf)
#### [15]
Lim, J., Reps, T., Liblit, B.: Extracting output formats from executables. In: 13th Working Conference on Reverse Engineering, 2006. WCRE ’06, pp. 167–178. IEEE, Benevento (2006). doi:10.1109/WCRE.2006.29 [PDF](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.138.3603&rep=rep1&type=pdf)
#### [16]
I. Bermudez, A. Tongaonkar, M. Iliofotou, M. Mellia, and M. M. Munafo, “Automatic protocol field inference for deeper protocol understanding,” in Proceedings of the 14th IFIP Networking Conference (Networking ’15), pp. 1–9, May 2015. [PDF](http://dl.ifip.org/db/conf/networking/networking2015/1570062733.pdf)
#### [17]
Campana, G.: Fuzzgrind: an automatic fuzzing tool. In: Hack. lu. Hack. lu, Luxembourg (2009)
#### [18]
N. Borisov, D. J. Brumley, H. J. Wang, J. Dunagan, P. Joshi, and C. Guo, “Generic application-level protocol analyzer and its language,” MSR Technical Report MSR-TR-2005-133, 2005. [PDF](http://www.academia.edu/download/31148072/2005-133.pdf)
#### [19]
[1]Y.-H. Goo, K.-S. Shim, M.-S. Lee, and M.-S. Kim, “Protocol Specification Extraction Based on Contiguous Sequential Pattern Algorithm,” IEEE Access, vol. 7, pp. 36057–36074, 2019, doi: 10.1109/ACCESS.2019.2905353.  [PDF](https://ieeexplore.ieee.org/iel7/6287639/6514899/08667834.pdf)
#### [20]
Slowinska, A., Stancescu, T., Bos, H.: Howard: a dynamic excavator for reverse engineering data structures. In: Proceedings of the 18th Annual Network and Distributed System Security Symposium (NDSS). Internet Society, San Diego (2011)
#### [21]
[1]X. Wang, K. Lv, and B. Li, “IPART: an automatic protocol reverse engineering tool based on global voting expert for industrial protocols,” International Journal of Parallel, Emergent and Distributed Systems, vol. 35, no. 3, pp. 376–395, May 2020, doi: 10.1080/17445760.2019.1655740. 
#### [22]
P. Laroche, A. Burrows, and A. N. Zincir-Heywood, “How far an evolutionary approach can go for protocol state analysis and discovery,” in Proceedings of the IEEE Congress on Evolutionary Computation (CEC ’13), pp. 3228–3235, June 2013.
#### [23]
Cho, C.Y., Babi D., Shin, E.C.R., Song, D.: Inference and analysis of formal models of botnet command and control protocols. In: Proceedings of the 17th ACM Conference on Computer and Communications Security, CCS ’10, pp. 426–439. ACM, New York, NY (2010). doi:10.1145/1866307.1866355
Cho, C.Y., Babi, D., Poosankam, P., Chen, K.Z., Wu, E.X., Song, D.: MACE: model-inference-assisted concolic exploration for protocol and vulnerability discovery. In: Proceedings of the 20th USENIX Conference on Security, SEC’11, p. 19. USENIX Association, Berkeley, CA (2011)
#### [24]
J. Ma, K. Levchenko, C. Kreibich, S. Savage, and G. Voelker, “Automatic protocol inference: unexpected means of identifying protocols,” UCSD Computer Science Technical Report CS2006-0850, 2006. [PDF](http://www.academia.edu/download/38268/2q7zdptm5klmgg2h0g9.pdf)
#### [25]
F. Meng, Y. Liu, C. Zhang, T. Li, and Y. Yue, “Inferring protocol state machine for binary communication protocol,” in Proceedings of the IEEE Workshop on Advanced Research and Technology in Industry Applications (WARTIA ’14), pp. 870–874, September 2014.
#### [26]
G. Bossert, F. Guihéry, and G. Hiet, “Towards automated protocol reverse engineering using semantic information,” in Proceedings of the 9th ACM Symposium on Information, Computer and Communications Security, Kyoto, Japan, June 2014.
G. Bossert and F. Guihéry, “Reverse and simulate your enemy botnet C&C,” in Proceedings of the Mapping a P2P Botnet with Netzob, Black Hat 2012, Abu Dhabi, UAE, December 2012. [PDF](https://www.amossys.fr/upload/publication.pdf)
#### [27]
M. Shevertalov and S. Mancoridis, “A reverse engineering tool for extracting protocols of networked applications,” in Proceedings of the 14th Working Conference on Reverse Engineering (WCRE ’07), pp. 229–238, October 2007.
#### [28]
M. Beddoe, “The protocol informatics project,” 2004, http://www.4tphi.net/∼awalters/PI/PI.html. [PDF](http://www.4tphi.net/~awalters/PI/pi.pdf)
#### [29]
Krueger, T., Gascon, H., Krmer, N., Rieck, K.: Learning stateful models for network honeypots. In: Proceedings of the 5th ACM Workshop on Security and Artificial Intelligence, AISec ’12, pp. 37–48. ACM, New York, NY (2012). doi:10.1145/2381896.2381904
#### [30]
[1]H. Gascon, C. Wressnegger, F. Yamaguchi, D. Arp, and K. Rieck, “Pulsar: Stateful Black-Box Fuzzing of Proprietary Network Protocols,” in Security and Privacy in Communication Networks, vol. 164, B. Thuraisingham, X. Wang, and V. Yegneswaran, Eds. Cham: Springer International Publishing, 2015, pp. 330–347.  [PDF](http://user.cs.uni-goettingen.de/~krieck/docs/2015-securecomm.pdf)
#### [31]
J. Caballero, H. Yin, Z. Liang, and D. Song, “Polyglot: automatic extraction of protocol message format using dynamic binary analysis,” in Proceedings of the 14th ACM Conference on Computer and Communications Security (CCS ’07), pp. 317–329, ACM, November 2007.
#### [32]
D. R. Fletcher Jr., Identifying Vulnerable Network Protocols with PowerShell, SANS Institute Reading Room site, 2017.
#### [33]
Y. Wang, X. Yun, M. Z. Shafiq et al., “A semantics aware approach to automated reverse engineering unknown protocols,” in Proceedings of the 20th IEEE International Conference on Network Protocols (ICNP ’12), pp. 1–10, IEEE, Austin, Tex, USA, November 2012.
#### [34]
Q. Huang, P. P. C. Lee, and Z. Zhang, “Exploiting intrapacket dependency for fine-grained protocol format inference,” in Proceedings of the 14th IFIP Networking Conference (NETWORKING ’15), Toulouse, France, May 2015.
#### [35]
Y. Wang, X. Yun, Y. Zhang, L. Chen, and T. Zang, “Rethinking robust and accurate application protocol identification,” Computer Networks, vol. 129, pp. 64–78, 2017.
#### [36]
Y. Wang, X. Yun, Y. Zhang, L. Chen, and G. Wu, “A nonparametric approach to the automated protocol fingerprint inference,” Journal of Network and Computer Applications, vol. 99, pp. 1–9, 2017.
#### [37]
C. Rossow and C. J. Dietrich, “PROVEX: detecting botnets with encrypted command and control channels,” in Detection of Intrusions and Malware, and Vulnerability Assessment, Springer, 2013. [PDF](https://chrisdietri.ch/files/provex-dimva2013.pdf)
#### [38]
P. M. Comparetti, G. Wondracek, C. Kruegel, and E. Kirda, “Prospex: protocol specification extraction,” in Proceedings of the 30th IEEE Symposium on Security and Privacy, pp. 110–125, Berkeley, Calif, USA, May 2009.
#### [39]
Lin, Z., Zhang, X., Xu, D.: Automatic reverse engineering of data structures from binary execution. In: Proceedings of the 17th Annual Network and Distributed System Security Symposium (NDSS). Internet Society, San Diego (2010)
#### [40]
J.-Z. Luo, S.-Z. Yu, and J. Cai, “Capturing uncertainty information and categorical characteristics for network payload grouping in protocol reverse engineering,” Mathematical Problems in Engineering, vol. 2015, Article ID 962974, 9 pages, 2015.
#### [41]
Z. Wang, X. Jiang, W. Cui, X. Wang, and M. Grace, “ReFormat: automatic reverse engineering of encrypted messages,” in Computer Security—ESORICS 2009. ESORICS 2009, M. Backes and P. Ning, Eds., vol. 5789 of Lecture Notes in Computer Science, pp. 200–215, Springer, Berlin, Germany, 2009.
#### [42]
Cui, W., Paxson, V., Weaver, N., Katz, R.H.: Protocol-independent adaptive replay of application dialog. In: Proceedings of the 13th Annual Network and Distributed System Security Symposium (NDSS). Internet Society, San Diego (2006). http://research.microsoft.com/apps/pubs/default.aspx?id=153197
#### [43]
J. Antunes, N. Neves, and P. Verissimo, “Reverse engineering of protocols from network traces,” in Proceedings of the 18th Working Conference on Reverse Engineering (WCRE ’11), pp. 169–178, October 2011.
#### [44]
W. Cui, V. Paxson, N. C. Weaver, and R. H. Katz, “Protocolindependent adaptive replay of application dialog,” in Proceedings of the 13th Symposium on Network and Distributed System Security (NDSS ’06), 2006. [PDF](https://www.ndss-symposium.org/wp-content/uploads/2017/09/Protocol-Independent-Adaptive-Replay-of-Application-Dialog-Weidong-Cui.pdf)
#### [45]
Caballero, J., Song, D.: Rosetta: Extracting Protocol Semantics Using Binary Analysis with Applications to Protocol Replay and NAT Rewriting. Technical Report CMU-CyLab-07-014, Carnegie Mellon University, Pittsburgh (2007)
#### [46]
C. Leita, K. Mermoud, and M. Dacier, “ScriptGen: an automated script generation tool for Honeyd,” in Proceedings of the 21st Annual Computer Security Applications Conference (ACSAC ’05), pp. 203–214, Tucson, Ariz, USA, December 2005. [PDF](https://www.researchgate.net/profile/Marc_Dacier/publication/4207362_ScriptGen_an_automated_script_generation_tool_for_Honeyd/links/02e7e52f3691fd9dbb000000/ScriptGen-an-automated-script-generation-tool-for-Honeyd.pdf)
#### [47]
[1]K. Shim, Y. Goo, M. Lee, and M. Kim, “Clustering method in protocol reverse engineering for industrial protocols,” International Journal of Network Management, Jun. 2020, doi: 10.1002/nem.2126.  [PDF](https://nmlab.korea.ac.kr/publication/published.papers/2020/2020.06_Clustering_method_for_ICS-APRE-IJNM.pdf)
#### [48]
[1]F. Sun, S. Wang, C. Zhang, and H. Zhang, “Clustering of unknown protocol messages based on format comparison,” Computer Networks, vol. 179, p. 107296, Oct. 2020, doi: 10.1016/j.comnet.2020.107296. 
#### [49]
A. Trifilo, S. Burschka, and E. Biersack, “Traffic to protocol reverse engineering,” in Proceedings of the IEEE Symposium on Computational Intelligence for Security and Defense Applications, pp. 1–8, July 2009.
#### [50]
W. Cui, M. Peinado, K. Chen, H. J. Wang, and L. Irun-Briz, “Tupni: automatic reverse engineering of input formats,” in Proceedings of the 15th ACM Conference on Computer and Communications Security (CCS ’08), pp. 391–402, ACM, Alexandria, Va, USA, October 2008.
#### [51]
R. Lin, O. Li, Q. Li, and Y. Liu, “Unknown network protocol classification method based on semi supervised learning,” in Proceedings of the IEEE International Conference on Computer and Communications (ICCC ’15), pp. 300–308, Chengdu, China, October 2015.
#### [52]
Y. Wang, Z. Zhang, D. D. Yao, B. Qu, and L. Guo, “Inferring protocol state machine from network traces: a probabilistic approach,” in Proceedings of the 9th Applied Cryptography and Network Security International Conference (ACNS ’11), pp. 1–18, 2011.
#### [53]
K. Choi, Y. Son, J. Noh, H. Shin, J. Choi, and Y. Kim, “Dissecting customized protocols: automatic analysis for customized protocols based on IEEE 802.15.4,” in Proceedings of the 9th ACM Conference on Security and Privacy in Wireless and Mobile Networks, pp. 183–193, Darmstadt, Germany, July 2016.
#### [54]
Y. Wang, N. Zhang, Y.-M. Wu, B.-B. Su, and Y.-J. Liao, “Protocol formats reverse engineering based on association rules in wireless environment,” in Proceedings of the 12th IEEE International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom ’13), pp. 134–141, Melbourne, Australia, July 2013.
#### [55]
M.-M. Xiao, S.-Z. Yu, and Y. Wang, “Automatic network protocol automaton extraction,” in Proceedings of the 3rd International Conference on Network and System Security (NSS ’09), pp. 336–343, October 2009.
#### [56]
[1]C. Yang, C. Fu, Y. Qian, Y. Hong, G. Feng, and L. Han, “Deep Learning-Based Reverse Method of Binary Protocol,” in Security and Privacy in Digital Economy, vol. 1268, S. Yu, P. Mueller, and J. Qian, Eds. Singapore: Springer Singapore, 2020, pp. 606–624. 
#### [57]
Z. Zhang, Q.-Y. Wen, and W. Tang, “Mining protocol state machines by interactive grammar inference,” in Proceedings of the 2012 3rd International Conference on Digital Manufacturing and Automation (ICDMA ’12), pp. 524–527, August 2012.
