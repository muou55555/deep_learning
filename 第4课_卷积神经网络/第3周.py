# 第3.3课内容
滑动窗口目标检测法：
	首先选定一个特定大小的窗口，将这个窗口（从图片左上角开始）输入卷积网络，卷积网络开始进行预测，即判断该窗口内有没有汽车，
	然后将窗口稍向右滑动，并输入给卷积网络，检测这一个窗口内有没有汽车。即每次输入进卷积网络的只是这张大图片的某个小窗口范围内
	的图片。依次重复操作直到这个窗口滑过图像的每一个角落，对每个窗口位置的图片按0和1进行分类（即有或没有目标）。
	为了滑动得更快，可以选用较大的步幅。
	也可以选取更大的窗口进行滑动。
	
滑动窗口目标检测法有很明显的缺点，就是计算成本。因为你在图片中剪切出太多小方块，卷积网络要一个一个地处理。如果选用的步幅很大，
显然会减少输入卷积神经网络的窗口个数，但是粗粒度可能会影响性能。反之，如果采用小粒度或小步幅，传递给卷积网络的小窗口会特别多，
这意味着超高的计算成本。

所以在神经网络兴起之前，人们通常采用更简单的分类器进行对象检测，比如简单的线性分类器。至于误差，因为每个分类器的计算成本都很低，
它只是一个线性函数，所以滑动窗口目标检测算法表现很好。然而，卷积网络运行单个分类任务的成本却高得多，像这样滑动窗口太慢了。除非
采用超细力度或极小步幅，否则无法准确定位图片中的对象。不过，庆幸的是，计算成本问题已经有了很好的解决方案，大大提高了在卷积层上
应用滑动窗口目标检测器的效率。

----------------------------------------------------------------------------------------------------------------------------------
#第3.4课内容

把全连接层转化成卷积层：
比如 使用5*5的过滤器，在全连接层来实现卷积，若全连接层的前一层图像是5*5*16，全连接层有400个节点就使用400个5*5*16的过滤器对图像
进行卷积得到输出维度为1*1*400，我们不再把它看做一个含有400个节点的集合，而是一个1*1*400地输出层。从数学角度看，他和全连接层是一
样的，因为这400个节点中的每一个节点都有一个5*5*16维度的过滤器，所以每个值都是上一层这些5*5*16激活值经过某个任意线性函数的输出结果。
不管原来有几个全连接层，每个全连接层都可以这样转化成卷积层。

#【疑问】
为什么要把全连接层转化成卷积层呢？把图片拉成一个向量有什么不好？那么多过滤器，过滤器的参数都是一个个的慢慢训练数据得到的吗？
难道进行卷积速度会特别快？

#在卷积层上应用滑动窗口算法的内容，它提高了整个算法的效率。这种算法有个缺点，就是边界框的位置可能不够准确。
假设输入给卷积网络的图片大小是14*14*3，测试集图片是16*16*3，按照上节课的滑动窗口检测法，是先从左上角滑动，步幅为2，这样就有
四个子集。结果发现这四次卷积操作中的很多计算都是重复的。滑动窗口的卷积应用，使得卷积网络在这四次操作过程中很多计算都是重复的。
最终，在输出层这2*2的四个子方块中，蓝色的是图像左上部分14*14的输出。

所以该卷积操作的原理是：
我们不需把输入图片分割成四个子集分别执行前向传播，而是把它们作为一张图片输入给卷积网络进行计算，其中的公有区域可以共享很多计算。

我们不用依靠连续的卷积操作来识别图片中的汽车，我们可以对大小为28*28的整张图片进行卷积操作，一次得到所有预测值。

----------------------------------------------------------------------------------------------------------------------------------
# 第3.5课内容
# 指定边界框
# YOLO算法
对于不使用滑窗法检测整张图片中的目标，方法是把整张图片分割为3*3或者19*19块，然后对每一块都进行卷积，但不是依次卷积，而是最终得到了
比如你把图片分割了3*3块，最终就得到了3*3*n的最终输出，输出层的3*3*n的9个向量(n维向量)对应于分割为3*3块的各块，由于3*3块，则每块最终
输出的向量是由【是否有目标，以及目标中心位置，以及目标的边框长度宽度，有没有别的目标】等等组成。

这样就不需要使用滑窗法依次滑动输入卷积神经网络了来进行识别了。

YOLO算法实时性挺好。
