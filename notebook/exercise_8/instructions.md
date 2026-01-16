**Homework — MNIST ↔ MNIST-A and Transfer Learning**  
In class, we:

* Loaded and inspected the MNIST-A dataset  
* Identified and fixed defects in the image orientation  
* Built an MNIST-A dataloader compatible with MNIST  
* Trained a small CNN (CNNM) on MNIST  
* Evaluated it on MNIST-A **without retraining**, and observed a major drop in performance  
* Analyzed the errors using a confusion matrix

In this homework, you will **extend and complete the investigation**.

**Part 1 — Baselines (reproducible experiments)**

Using the provided CNNM architecture:  
**1\.**

**Train CNNM on MNIST**

* Report training and test performance over time.  
* Make sure the model does not overfit.  
* Include at least one plot (loss and/or accuracy).

**2\.  Train a fresh CNNM from scratch on MNIST-A**

* Use the same architecture and comparable training settings.  
* Report training and test performance over time.  
* Compare convergence speed and final accuracy to MNIST.

Briefly explain:

* Why MNIST-A is harder (or different) than MNIST.  
* Which digits appear most problematic.

**Part 2 — Transfer Learning experiments**

Now we will investigate whether we can improve performance on MNIST-A.

**3\. Train CNNM on MNIST (source task)**

* Start from random initialization.  
* Train until reasonable MNIST performance is reached.

**4\.  Create two copies of the trained model**
***Experiment A — No freezing***

* Continue training the model on **MNIST-A**  
* Do not delete or freeze any layers.  
* Track performance over time.

Answer:

* How fast does the model adapt?  
* What happens if you test this model back on MNIST?  
* Do you observe catastrophic forgetting?

***Experiment B — Freeze feature extractor***

* Freeze all layers **except the final fully connected layers.**
* Retrain on MNIST-A.  
* Track performance over time.

Answer:

* How long does training take compared to Experiment A?  
* Does the model reach similar accuracy faster?  
* How does final performance compare?

**Part 3 — Discussion (conceptual)**

In your own words, explain:

* Why Transfer Learning helps in this setting.  
* Why freezing layers can speed up training.  
* Why freezing too much might hurt performance.  
* What this tells us about the features learned from MNIST.

You may include:

* Plots  
* Confusion matrices  
* Example predictions

Focus on **reasoning and interpretation** , not just numbers.

Notes

* You may reuse code from class where appropriate.  
* You are welcome to consult AI tools (e.g. ChatGPT) for research or debugging, but your explanations must be in your own words.  
* Clean, well-organized notebooks will be graded more favorably than long, unstructured ones.

**Goal of this assignment:**  
To understand how domain shift affects neural networks, and how Transfer Learning can mitigate it — not by magic, but by reusing representations intelligently.

\-------------------------------------------  
**Bonus Exercise — Transfer Learning with ResNet18 (Advanced)**  
This bonus exercise extends the previous work by using a

**modern pretrained backbone** instead of a small custom CNN.  
This part is optional, but strongly recommended if you want hands-on experience with transfer learning workflows.

**Goal**

To observe how a **pretrained ResNet** net behaves on:

* MNIST  
* MNIST-A

and compare its behavior to the custom CNNM.

**Setup**

* Use **ResNet18 pretrained on ImageNet**.  
* Adapt it to classify **10 digits**.  
* Adjust the input pipeline as needed so MNIST / MNIST-A images are compatible.

**Notes:**

* ResNet expects

  **3-channel images** .  
* ResNet typically expects larger images (e.g. 224×224), but reasonable resizing is sufficient.  
* You may reuse your existing dataloaders with appropriate transforms.

**Part 1 — Baseline with ResNet18**

**1\.  Load a pretrained ResNet18**  

* Replace the final classification layer so the output has 10 classes.  
* Freeze all backbone layers.

**2\. Train only the final layer on MNIST**

* Train for a small number of epochs.  
* Report training and test performance.

Answer briefly:

* How fast does the model converge?  
* How does this compare to CNNM trained from scratch?

Part 2 — Domain shift with ResNet18

**3\. Evaluate the MNIST-trained ResNet18 on MNIST-A**

* Do retrain yet.  
* Report accuracy and (optionally) a confusion matrix.

Answer:

* Does ResNet18 generalize better than CNNM?  
* Which digits still fail?

**Part 3 — Transfer Learning on MNIST-A**

**4\. Transfer to MNIST-A (two strategies)**

Experiment A — No freezing

* Continue training the entire ResNet18 on MNIST-A.  
* Track performance over time.

Experiment B — Partial freezing

* Freeze most of the backbone.  
* Unfreeze only the last block (e.g. layer4) and the classifier.  
* Retrain on MNIST-A.

Answer:

* Which strategy converges faster?  
* Which achieves higher final accuracy?  
* How does this compare to CNNM transfer learning?

**Discussion**

Briefly explain:

* Why a pretrained ResNet transfers better (or not) than CNNM.  
* What kinds of features ResNet might already have learned that help with digits.  
* When using a large pretrained model is , and when it might be overkill.

Notes

* This is an

  **advanced / bonus** task.  
* Partial completion is fine.  
* Focus on  **observations and reasoning**, not perfect results.  
* Clear explanations matter more than squeezing out extra accuracy.

**Takeaway:**

This exercise connects classroom concepts to how Transfer Learning is actually done in real-world projects — using large pretrained backbones and adapting them efficiently to new domains.
