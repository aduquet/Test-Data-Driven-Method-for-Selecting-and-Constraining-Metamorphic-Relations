# A Fuzzer Based Approach For Selecting MRs 

Metamorphic Testing (MT) is a testing technique that can effectively alleviate the oracle problem. MT uses Metamorphic Relations (MRs) to determine if a test case passes or fails. MRs specify how the outputs should vary in response to specific input changes when executing the System Under Test (SUT). If a particular MR is violated for at least one test input (and its change), there is a high probability that the SUT has a fault. On the other hand, if a particular MR is not violated, it does not guarantee that the SUT is fault free. Currently, MRs are handpicked and require in-depth knowledge of the System Under Test (SUT), as well as its problem domain. As a result, the identification and selection of high-quality MRs is a challenge.

Kanewala et al. suggested the Predicting Metamorphic Relations (PMR) approach for automatic prediction of applicable MRs picked from a predefined list. PMR is based on a Support Vector Machine (SVM) model using features derived from the Control Flow Graphs (CFGs) of 100 Java methods. The original study of Kanewala et al. showed encouraging results, but developing classification models from CFG-related features is costly. Also, it is required to have a labelled data set with the ground true to train the models.

# Repository Organization

- Folder 'AllMethod' Stores all the methods used. Those mehtods are written in Java and Python.
- Folder 'FirstExp': 
