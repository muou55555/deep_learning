
#本周内容：深度学习的使用层面

【0】总结一下，在机器学习中，我们通常将样本分成训练集、验证集和测试集三部分。数据集规模相对较小的，适用传统的划分比例60%,20%,20%；
	数据规模较大的，验证集和测试集可以占到数据总量的20%或10%以下.例如100万条数据，1万条作验证集，1万条作测试集，训练集占98%。
	验证集是用来评估不同的模型；测试集是对最终所选定的神经网络系统做出【无偏评估】。如果不需要无偏评估，也可以不设置测试集。
	如果只有验证集，没有测试集，我们要做的是，在训练集上训练，尝试不同的模型框架，在验证集上评估这些模型，然后迭代并选出适用的模型。
	因为验证集中已经涵盖测试集数据，其不再提供无偏性能估计。
	在机器学习中，如果只有一个训练集和一个验证集，而没有独立的测试集，则验证集被称为测试集。不过在实际应用中，人们只是把测试集当成
	简单交叉验证集使用，并没有完全实现该术语的功能，因为他们把验证集数据过度拟合到了测试集中。如果某团队跟你说他们只设置了一个训练集
	和一个测试集，我会很谨慎，心想他们是不是真的有训练验证集，因为他们把验证集数据过度拟合到了测试集中，让这些团队改变叫法，
	改称其为"训练验证集"，而不是"训练测试集"可能不太容易，即便我认为在专业用词上更准确。实际上，如果你不需要无偏评估算法性能，
	那么这样是ok的。
	
【1】深度学习的另一个趋势是，越来越多的人在训练集和测试集分布不匹配的请情况下进行训练，假设你要构建一个用户可以上传大量图片的应用程序，
	目的是找出并呈现所有的猫咪图片，训练集可能是从网上下载的猫咪图片，而验证集和测试集是用户在这个应用上上传的猫咪的图片。
	就是说，训练集可能是从网上抓下来的图片，分辨率很高，而验证集和测试集使用户上传的图片（可能是手机随意拍摄的），分辨率很低，比较模糊。
	这两类数据有所不同。根据经验，我建议大家 要确保验证集和测试集的数据来自同一分布。
	
【2】偏差和方差   bias/variance
	偏差高，不能很好的拟合数据集，欠拟合    举的例子图是二分类logistic
	分类器方差较高，数据过度拟合，过拟合    举的例子图是神经网络过拟合分类的图
	
	训练集误差和验证集误差  train set error  /   dev set error
	(1)训练集误差(1%)低，验证集误差(11%)高，则称之为高方差
	(2)训练集数据的拟合度不高，就是数据欠拟合，就可以说这种算法偏差比较高；
		相反，他对于验证集产生的结果却是合理的，验证集中的错误率(16%)只比训练集的错误率(15)多1%，所以这种算法偏差高.
	(3)训练集错误率是15%，偏差相当高，但是验证集的评估结果更糟糕，错误率达到30%。
		这种情况下，我会认为这种算法偏差高，因为它在训练集上结果不理想，方差也很高，这是方差偏差都很高的情况。
	(4)训练集错误率为0.5%，验证集错误率为1%，则方差和偏差都很低。
			
	一般来说，最优误差也被称为贝叶斯误差
	# 如果最优误差或贝叶斯误差非常高，比如15%，15%的错误率对训练集来说是非常合理的，偏差不高，方差也非常低。【感觉这句话有问题，我没理解】

	先检查偏差，再检查方差：
	(1)如果偏差高，(欠拟合)，就试一下:1.选择一个新网络(比如含有更多隐藏层或者隐藏单元的网络)。2.花费更多的时间来训练网络，
		或者尝试更先进的优化算法。    不过【采用规模更大的网络】通常会有所帮助，延长训练时间不一定有用，但也没什么坏处。
		训练学习算法时，需要不断尝试这些方法，直到解决掉偏差问题，这是最低标准，反复尝试，直到可以拟合数据为止。
		至少能够拟合训练集。如果网络足够大，通常可以很好的拟合训练集。
	(2)当偏差降低到可接受的数值，检查一下方差有没有问题，为了评估方差，我们要查看验证集性能；
		如果方差高，最好的解决方法就是【采用更多数据】。但有时候，我们无法获得更多数据，我们也可以尝试通过【正则化】来减少过拟合。
	(3)反复各种尝试，直到找到一个低偏差，低方差的框架，这样你就成功了。
	
	有两点需要注意：
	(1)高偏差和高方差是两种不同的情况，我们后续要尝试的方法也可能完全不同。我们通常会用训练验证集来诊断算法是否存在偏差
		或方差问题。，然后根据结果选择尝试部分方法。
		举个例子，如果算法存在【高偏差问题】，准备【更多训练数据其实什么用都没有】。所以大家要清楚到底是高方差还是高偏差问题。
		明确这一点有助于我们选出最有效的方法。
	(2)在机器学习的初期阶段，关于偏差方差权衡的探讨屡见不鲜。原因是我们可以尝试的方法有很多，可以增加偏差，减少方差。
		但是在深度学习的早期阶段，我们没有太多工具可以做到只减少偏差或方差，却不影响到另一个。但是在当前的深度学习和大数据时代，
		只要持续训练一个更大的网络，只要准备了更多数据，那么也并非只有这两种情况。
		只要正则适度，通常构建一个更大的网络便可以在不影响方差的同时，减少偏差。而采用更多数据通常可以在不过多影响偏差的同时减少方差。
		这两步实际要做的工作是训练网络、选择网络或者准备更多数据，现在我们有工具可以做到在只减少偏差的同时，不对另一方产生过多不良影响。
		我觉得这就是深度学习对监督式学习大有裨益的一个重要原因。也是我们不用太过关注如何平衡偏差和方差的一个重要原因。
		
【3】正则化-------------------第二课--第一周--1.4-正则化
	【3.1】以logistic回归为例：(与神经网络的区别是logistic回归相当于只有一层的神经网络)
		【L1正则化】：R(w)=λ/m*|w|，    其中|w|是1范数
		【L2正则化】：R(w)=λ/2m*||w||^2    其中||w||是二范数，并且||w||^2=w^T*w
		
		代价函数：
			J(w,b)=1/m *ΣL(a(i),y)
			J(w,b)=-1/m *Σ[y(i)log(a(i))+(1-y(i))log(1-a(i))]
		
		加入L2正则化的代价函数：
			J(w,b)=-1/m *Σ[y(i)log(a(i))+(1-y(i))log(1-a(i))] + λ/2m*||w||^2
	
	【3.2】以神经网络为例：
		在神经网络中实现带L2正则化的过程：
		L2正则化:R(w) = λ/2m*Σ||w^[l]||F^2
			正则化项中的Σ求l=1到l=L层。w^[l]表示第l层的所有权重.每层的权重组成一个矩阵。
			||w^[l]||F^2 被定义为矩阵中所有元素的平方求和。F是下标，指代弗罗贝尼乌斯范数，表示求矩阵中所有元素的平方和。
			
		成本函数：J(w,b)=1/m *ΣL(a(i),y(i)) + λ/2m*Σ||w^[l]||F^2，	
		成本函数中包含从w[1],b[1]到w[L],b[l]共L层的所有参数
			注意这里的||w[l]||F^2是神经网络的所有层的矩阵L2范数,称为Frobenius弗罗贝尼乌斯范数，
			||w^[l]||F^2是(l-1)层到l层的各个权重的平方之和ΣΣ(wij)^2，这里两个求和符号Σ分别遍历(l-1)的第i个神经元，另一个表示遍历
			第l层的第j个神经元。
			Σ||w[l]||F^2 = 所有层的各个权重的平方之和ΣΣΣ(wij)^2
			
	【3.3】如何使用弗罗贝尼乌斯范数实现【梯度下降】呢？
		答：用反向传播计算出dw的值，反向传播会给出∂J/∂w^[l]
		每层的梯度为：
			  dw^[l]=(...) + λ/m*w^[l], 其中(...)是正则化前面的项对w^[l]求导，不方便用式子表达出来。
										λ/m*w^[l]是正则化项R(w) = λ/2m*Σ||w^[l]||F^2对w^[l]求导得到的
		更新：w^[l] = w^[l]-α*dw^[l]
					= w^[l]-α*λ/m*w^[l]-α*(...)     #即与不加入L2正则化的区别是多了-α*λ/m*w^[l]
				#   =(1-α*λ/m)*w^[l]-α*(...)}   L2正则化也被称为'权重衰减',即权重指标乘以了一个小于1的系数，所以叫权重衰减。
	
	【3.4】为什么只正则化参数w?为什么不再加上参数b呢？
		答：因为w通常是一个高维参数矢量，已经可以表达高偏差问题，w可能含有很多参数，我们不可能拟合所有参数，而b只是单个数字。
		如果加上b，其实也没多大影响，因为b只是众多参数中的一个，所以通常省略b就行。
	
	【3.5】【L1正则化】与【L2正则化】的区别：
		(1)L1正则化会让参数w变得稀疏。所谓参数变得更稀疏是指会有更多的参数变为0，这样可以达到类似特征提取的功能。
		   L2正则化不会让参数w变得更稀疏的原因是当参数很小时(如0.001)，这个参数的平方基本商就可以忽略了，于是模型
		   不会进一步将这个参数调整为0。
		(2)L1正则化的计算公式不可导，而L2正则化公式可导。因为在优化参数时需要计算损失函数的偏导数，所以对
		   含有L2正则化损失函数的优化要更简洁，优化带L1正则化的损失函数要更加复杂，而且优化方法有很多种，
		   在实践中也可以将L1正则化和L2正则化同时使用: R(w)=Σ {α|w|+(1-α)w^2}					
	
	【3.6】为什么正则化有利于预防过拟合呢？为什么他可以减少方差问题？
		答：加入正则化后，把λ设置足够大，w^[l]设置足够小接近于0.直观理解就是把许多隐藏单元的权重设为0，于是基本消除了这些隐藏单元
		的许多影响，如果是这种情况，这个被大大简化了的神经网络会变成一个很小的网络，小到如同一个逻辑回归单元，可是深度却很大，它会
		使这个网络从过拟合状态更接近于高偏差状态，但是λ会存在一个中间值，即处于高方差和高偏差状态的正中间的'just right'的中间状态。
		直观理解就是λ增加到足够大，w会设置为接近于0。实际上不会发生这种情况的，我们尝试消除或者至少减少许多隐藏单元的影响，最终这个
		网络会变得更简单，这个神经网络越来越接近于逻辑回归。
		我们直觉上会认为大量隐藏单元被完全消除了，其实不然，实际上该神经网络的所有隐藏单元依然存在，但是他们的影响变得更小了，神经
		网络变得更简单了，貌似这样更不容易发生过拟合，吴恩达不确定这个直觉经验是否有用，不过在编程中执行正则化时，你会实际看到一些
		方差减少的结果。
		
		我的理解:过拟合的情况即得到了极复杂的高度非线性函数。防止过拟合就是使得到的函数不那么复杂，使其变成线性函数或者简单的曲线就行。
		
	【3.7】dropout(随机失活)-----非常实用的正则化方法：
		dropout会遍历网络的每一层，并设置消除神经网络中节点的概率。假设 网络中的每一层每个节点都以抛硬币的方式设置概率，每个节点得以
		保留和消除的概率都是0.5，设置完节点概率，我们会消除一些节点，然后删除从该节点进出的连线，最后得到一个节点更少、规模更小的网络，
		然后用backprop方法进行训练。 对于其他样本，我们照旧以抛硬币的方式设置概率，保留一类节点集合，删除其他类型的节点集合。对于每个
		训练样本，我们都将采用一个精简后的神经网络来训练它。这个方法可能有点奇怪，单纯遍历节点，编码也是随机的，可它真的有效。
		不过可想而知，我们针对每个样本训练规模极小的网络，最后你可能会认识到为什么要正则化网络，因为我们在训练极小的网络。
		
		实施dropout的方法：
		inverted dropout (反向随机失活)-------最常用的dropout方法
		以一个三层神经网络为例：
		只举例说明如何在某一层中实施dropout：
		d3=np.random.rand(a3.shape[0],a3.shape[1]) < keep_prob
		d3表示第三层的dropout向量
		keep_prob 表示保留某个隐藏单元的概率，如keep_prob=0.8意味着消除任意一个隐藏单元的概率是0.2，他的作用就是生成随机矩阵.
		如果对a3进行因式分解，效果也一样，d3是一个矩阵，每个样本和每个隐藏单元，其在d3中的对应值为1的概率都是80%，其在d3中的
		对应值为0的概率都是20%。随机数字小于0.8，它等于1的概率是0.8。
		
		接下来要做的就是从第三层中获取激活函数，这里我们叫他a3,a3含有要计算的激活函数，a3=np.multiply(a3,d3),这里是元素相乘，
		也可以写成a3*=d3,他的作用就是过滤d3中所有等于0的元素，而各个元素等于0的概率只有20%，乘法运算最终把d3中相应元素归零。
		如果用python实现该算法的话，d3则是一个布尔型数组，值为true和false，而不是1和0，乘法运算依然有效，python会把true和
		false翻译为1和0。    
		最后我们向外扩展a3，a3/=keep_prob。  
		方便起见，我假设第三隐层上有50个单元，在一维上a3是50，我们通过因子分解将它拆分成50*m维，保留和删除他们的概率分别是
		0.8和0.2，这意味着 最后被删除或归零的单元平均有10个，现在我们看下z[4],其中z[4]=w[4]*a[3]+b[4]，我们的预期是a[3]减少20%，
		也就是说 a[3]中有20%的元素被归零，为了不影响z[4]的期望值，我们需要w[4]*a[3]/0.8,它将会修正或弥补我们所需的那20%，
		a3的期望值不会变，
		a3/=keep_prob就是所谓的inverted dropout方法，它的功能是，不论keep_prob的值是多少，0.8,0.9甚至是1，如果keep_prob的值设置为1，
		那么就不存在dropout,因为它会保留所有节点。
		
		inverted dropout方法通过除以keep_prob,确保a3的期望值不变。事实证明,【在测试阶段，当我们评估一个神经网络时】,inverted dropout
		也就是a3/=keep_prob的反向随机失活方法使得测试阶段变得更容易，因为他的数据扩展问题变少。据吴恩达了解，目前实施dropout最
		常用的方法就是inverted dropout。dropout早期的迭代版本都没有除以keep_prob，所以在测试阶段，平均值会变得越来越复杂，不过
		那些版本已经不再使用了。  
		现在使用的是d向量，你会发现，【不同的训练样本，清除的隐藏单元也不同】。实际上，如果你通过相同训练集
		多次传递数据，每次训练数据的梯度不同，则随机对不同隐藏单元归零，【有时却并非如此】，比如，需要将相同隐藏单元归零，第一次迭代
		梯度下降时，把一些隐藏单元归零，【第二次迭代梯度下降时，也就是第二次遍历训练集时】，对不同类型的隐藏单元归零。向量d或d3用来
		决定第三层中哪些单元归零，无论用foreprop还是backprop，这里我们只介绍了foreprop.
		
		如何在测试阶段训练算法，在测试阶段，我们已经给出了x或是想预测的变量，用的是标准计数法，我用a[0]第0层的激活函数标注为测试
		样本x，我们【在测试阶段不使用dropout函数】，尤其是像下列情况：
		z[1]=w[1]*a[0]+b[1]
		a[1]=g[1](z[1])
		z[2]=w[2]*a[1]+b[2]
		a[2]=g[2](z[2])
		...
		以此类推直到最后一层，预测值为y^.
		显然在测试阶段，我们并未使用dropout，自然也就不用抛硬币来决定失活率，以及要消除哪些隐藏单元了。因为【在测试阶段进行预测时，
		我们不期望输出结果是随机的】。如果测试阶段应用dropout函数，预测会受到干扰。理论上，你只需要多次运行预测处理过程，每一次，
		不同的隐藏单元会被随机归零，预测处理遍历他们，但是计算效率低，得出的结果也几乎相同，与这个不同程序产生的结果极为相似。
		inverted dropout函数在除以keep_prob时可以记住上一步的操作，目的是确保在测试阶段不执行dropout来调整数值范围，激活函数
		的预期结果也不会发生变化，所以没必要在测试阶段额外添加尺度参数，这与训练阶段不同。
		
		第一个直观认识是：好像每次迭代后神经网络都会变得比以前更小，因此采用一个较小神经网络好像和使用正则化的效果是一样的。
		第二个直观认识是：我们从单个神经元(即第0层是输入层，有若干神经元，第一层只有一个神经元)入手，我们使用dropout，则该
		单元的输入几乎被删除，有时会删除其他单元，就是说第一层神经元不能依靠任何特征，因为特征都有可能被随机清除，或者说该
		单元的输入也都可能被随机清除。我不愿意把所有赌注都放在一个节点上，【不愿意给任何一个输入加上太多权重，因为他可能会被删除】。
		因此该单元将通过这种方式积极地传播开，并为单元的四个输入增加一点权重。通过传播所有权重，dropout将产生收缩权重的平方范数的效果。
		和我们之前讲过的L2正则化类似，实施dropout的结果是它会压缩权重，并完成一些预防过拟合的外层正则化。
		
		事实证明，dropout被正式地作为一种正则化的替代形式，L2对不同权重的衰减是不同的，它取决于倍增的激活函数的大小。
		
		总结一下，dropout的功能类似于L2正则化，与L2正则化不同的是，被应用的方式不同，dropout也会有所不同，甚至更适用于不同的输入范围。
		实施dropout的另一个细节是：不同层的keep_prob也可以变化，即每层keep_prob的值都可能不同。
		如果某层的权重规模较大,如该层权重矩阵为7*7，keep_prob可以设置为0.5;如果在某一层不需要关心过拟合问题,则该层keep_prob可设为1,
		意味着保留该层的所有单元，并且不再这一层使用dropout。对于有可能出现过拟合且含有诸多参数的层，我们可以把keep_prob设置为比较小
		的值来应用更强大的dropout. 有点像在处理L2正则化参数λ，我们尝试对某些层实施更多正则化，从技术上讲，我们也可以对输入层应
		用dropout,我们有机会删除一个或多个输入特征，虽然现实中我们通常不这么做，keep_prob的值为1，是非常常用的输入值，也可以用更大的值，
		或许是0.9，但是消除一般的输入特征是不太可能的。如果我们遵守这个准则，keep_prob的值会接近于1，即使你对输入层应用dropout。
		
		总结一下：如果你担心某些层比其它层更容易发生过拟合，可以把某些层的keep_prob值设置得比其它层更低。缺点是为了使用交叉验证，
		你要搜索更多的超级参数。
		另一种方案是在一些层上应用dropout，而有些层不使用dropout，应用dropout的层只含有一个超级参数，就是keep_prob。
		
		分享两个实施过程中的技巧：
		(1)计算机视觉中的输入量非常大，输入了太多像素，以至于没有足够的数据，所以dropout在计算机视觉中应用的比较频繁。
			但是要牢记一点：dropout是一种正则化方法，它有助于预防过拟合，因此，除非算法过拟合，不然我是不会使用dropout的，
			所以他在其他领域应用的比较少，主要存在于计算机视觉领域，因为我们通常没有足够的数据，所以一直存在过拟合，这就是
			有些计算机视觉研究人员如此钟情dropout方法的原因。直观上，我认为不能概括其他学科。
		(2)dropout一大缺点就是【代价函数J不再被明确定义】，每次迭代，都会随机移除一些节点，如果再三检查梯度下降的性能，实际上
			是很难进行复查的，定义明确的代价函数J每次迭代后都下降。因为我们所优化的代价函数实际上并没有明确定义，或者在某
			种程度上很难计算，所以我们失去了调试工具来绘制这样的图片。
		    下面的是实施dropout的技巧：我通常会关闭dropout,将keep_prob的值设为1，运行代码，【确保J函数单调递减】，然后再打开dropout，
			在dropout过程中，代码并未引入bug。
		
	【3.8】	其他正则化方法-----降低神经网络中的方差或者预防过拟合
	  (1)数据扩增-------解决过拟合问题
		以识别猫的图片为例子：
		扩增训练数据代价高，而且有时候我们无法扩增数据，可以通过：水平翻转图片、随意裁剪图片、旋转并放大后裁剪等方法，增大数据集，
		额外生成假训练数据。和全新的独立的图片数据相比，
		这些额外的假数据无法那么多信息，但是我们这么做基本没有花费，代价几乎为0，除了一些对抗性代价，以这种方式扩增算法数据，
		进而正则化数据集，减少过拟合比较廉价，像这样人工合成数据的话，我们要通过算法验证，翻转后的猫咪依然是猫，注意我们并没有垂直翻转，
		因为我们不想上下颠倒图片。也可以随机选取放大后的部分图片，猫可能还在上面。
		对于光学字符识别OCR，我们还可以通过添加数字，随意旋转或者扭曲数字来扩增数据，把这些数字添加到训练集。
		所以，数据扩增可作为正则化方法使用，实际功能上也与正则化相似。
	
	  (2)early stopping--------------提早停止训练神经网络。
		运行梯度下降时，我们可以绘制训练误差，或只绘制代价函数J的优化过程，在训练集上用0-1记录分类误差次数，呈单调下降趋势。
		因为在训练过程中，我们希望训练误差代价函数J都在下降，通过early stopping，我们不但可以绘制上面这些内容，还可以绘制验证集误差，
		它可以是验证集上的分类误差，或验证集上的代价函数、逻辑损失、对数损失等。你会发现，验证集误差通常会先呈下降趋势，然后在某个
		节点处开始上升。early stopping的作用就是在这个中间点停止迭代。
		
		early stopping的作用是：当你还未在神经网络上运行太多迭代过程的时候，参数w接近0，因为随机初始化w值时，它的值可能都是较小的
		随机值，所以在你训练神经网络For a long time之前，w依然很小.在迭代过程中和训练过程中，w的值会变得越来越大。
		
		所以early stopping要做的就是：
		在中间点停止迭代过程，我们得到一个w值中等大小的弗罗贝尼乌斯范数。与L2正则化相似，选择参数w范数较小的神经网络，但愿你的神经
		网络过拟合不严重。术语early stopping代表提早停止训练神经网络。
		
		early stopping的缺点是：你不能独立地处理这两个问题(即优化代价函数和防止过拟合)，因为提早停止梯度下降，也就是停止了优化代价
		函数J.因为现在你不再尝试降低代价函数J,所以代价函数J的值可能不够小。同时你又不希望出现过拟合，你没有采用不同的方法来解决这
		两个问题，而是用一种方法同时解决两个问题。这样做的结果是我要考虑的东西变得更复杂。
		
		如果不用early stopping,另一种方法就是L2正则化,训练神经网络的时间就可能很长。我发现,这导致超参数搜索空间更容易分解,也更容易
		搜索。但是缺点在于你必须尝试很多正则化参数λ的值，这也导致搜索大量λ值得计算代价太高。
		
		early stopping的优点是	：只运行一次梯度下降，你可以找出w的较小值、中间值和较大值，而无需尝试L2正则化超参数λ的很多值。
		吴恩达更倾向于使用L2正则化，尝试许多不同的λ值，假设你可以负担大量计算的代价。而使用early stopping也能得到相似结果，还不用
		尝试这么多值。
		
	【3.9】归一化输入
	训练神经网络，其中一个加速训练的方法就是：归一化输入。
	归一化输入需要两个步骤：
	1.零均值化
		μ=1/m*∑x^(i),    x^(i)是第i个样本，∑x^(i)即每个样本的特征对应相加，得到的向量μ的每个元素即是所有样本对应特征的均值
		x=x-μ,	x等于每个训练样本x-μ。这句话意思是移动训练集，直到它完成零均值化
		x,μ都是一个向量，因为每个样本x^(i)有若干特征，所以每个样本x^(i)是向量，那么μ就是向量，x也是向量
	2.归一化方差
		σ^2=1/m*∑x^(i)**2,	∑x^(i)**2是每个样本的对应特征元素的平方之和
		x/=σ^2	
		σ^2是一个向量，它的每个特征都有方差。注意我们已经完成零均值化，x^(i)**2，元素y^2就是方差，我们把所有数据都除以向量σ^2，
		即最后所有样本每个维度的特征的方差都等于1。用图像来帮助理解，即所有样本在图上，他们的每个维度上的特征方差都为1.
		
	如果用它来调整训练数据，那么用相同的μ和σ^2来归一化测试集，尤其是，你不希望训练集和测试集的归一化有所不同，不论μ和σ^2的值是什么，
	这两个公式中，你都会用到他们，所以你要用同样的方法调整测试集，而不是在训练集和测试集上分别预估μ和σ^2。因为我们希望不论是
	训练数据还是测试数据，都是通过相同的μ和σ^2定义的相同数据转换，其中μ和σ^2是由训练数据计算得来的。
	
	为什么要归一化输入？
	例如样本有两个特征输入(x1,x2),特征x1取值范围从0到10000,特征x1取值范围从0到1,结果是参数w1和w2值得范围或比率将会非常不同。
	优化代价函数时，非归一化特征输入的代价函数看起来想一个狭长的碗，对其运行梯度下降，你必须用一个非常小的学习比率，迭代次数也会很多；
	而归一化特征输入的代价函数看起来更对称，梯度下降法能够更直接的找到最小值，你可以在梯度下降法中使用较大步长，迭代次数会少很多。
	当然，实际上w是一个高维向量，因此用二维绘制w只是为了让我们更方便理解。
	
	如果输入特征处于不同范围内，那么归一化特征值就非常重要了;如果输入特征处于相似范围内，那么归一化特征值就不是很重要了。

【4】初始化权重
	【4.1】先看只有一个神经元的情况：
	单个神经元可能有4个输入特征,从x1到x4,经过a=g(z)处理，最终得到y^。
	z=w1*x1 + w2*x2 + ... + wn*xn,  b=0暂时忽略b
	为了预防z值过大或过小，输入神经元个数n越大，你就希望wi越小(因为预防z过大,n越大,w1到wn的个数就越多，只有wi越小才能防止z过大)。
	最合理的方法就是设置wi=1/n。  实际上你要做的就是设置某层权重矩阵w[l]=np.random.randn(_,_)*sqrt(1/(n[l-1]))。
	
	如果你用的是Relu激活函数，而不是1/n，那么方差设置为2/n效果会更好,w[l]=np.random.randn(_,_)*sqrt(2/(n[l-1]))。
	你常常发现，初始化时，尤其是使用Relu激活函数时,g[l](z)=Relu(z),它取决于你对随机变量的熟悉程度，这是高斯随机变量，然后乘以他
	的平方根，也就是引用这个方差2/n。
	
	这里我用的是n[l-1]因为本例中逻辑回归的特征是不变的。但一般情况下，l层上的每个神经元都有n(l-1)个输入。如果激活函数的输入特征
	被零均值化和标准方差(方差为1)，z也会调整到相似范围，这就没解决问题，但它确实降低了梯度消失和爆炸问题，因为它给权重矩阵w设置
	了合理值，它不能比1大很多，也不能比1小很多，所以梯度没有爆炸或消失过快。
	对于tanh激活函数来说,常量1比常量2的效率更高,对tanh函数来说,它是1/n[l-1]的平方根即。这里平方根的作用与上面的w[l]相同。
	还有另一种方法，使用公式2/(n[l-1]+n[l])的平方根。
	
【5】如何对计算梯度做数值逼近
	答：使用双边误差来判断别人给你的函数g(θ)是否正确实现了函数f的偏导
	在θ点处的梯度g(θ)近似等于g(θ)= [f(θ+ε)-f(θ-ε)]/2ε
	如：θ=1，ε=0.01,f(θ)=θ^3时，θ=1处的梯度g(1)=(1.01^3-0.99^3) / (2*0.01) =3.0001,而直接对f(θ)求导，正好g(1)=3*θ^2=3。
	所以这两个g(θ)值非常接近，逼近误差为0.0001。
	使用双边误差的方法比使用单边公差的方法更逼近导数。----单边是只针对f(θ)到f(θ+ε)或只针对f(θ-ε)到f(θ)来说的。
	在梯度检验和反向传播中使用双边误差的方法时，他与运行两次单边公差的速度一样。
		
【6】如何在backprop中执行梯度检验，以确保backprop正确实施
	梯度检验帮我节省了很多时间，也多次帮我发现backprop实施过程中的bug
	为了执行梯度检验，首先要做的就是 把所有参数w[1],b[1],...,w[L],b[L]转换成一个巨大的向量数据。你要做的就是把矩阵w转换成一个向量，
	然后做连接运算，得到一个巨型向量θ.代价函数J是所有W和b的函数，现在你得到了一个θ的代价函数J，接着你得到与w和b顺序相同的数据。
	你也可以把dw[1]和db[1],...,dw[L],db[L],用他们来初始化大向量dθ，，它与θ具有相同纬度。同样的，把dw[1]转换成矩阵，db[1]已经是一个
	向量了。直到把dw[L]转换成矩阵，这样所有的dw都已是矩阵。注意dw[1]与w1具有相同的维度，db[1]与b1具有相同的维度。经过相同的转换和
	连接运算操作后，你可以把所有导数转换成一个大向量dθ.
	现在的问题是dθ与代价函数J的梯度有什么关系，这就是实施梯度检验的过程。英文里通常简称为"grad check"
	J可以写作J(θ1,θ2,...),不论超参数向量θ的维度是多少。为了实施梯度检验，你要做的就是循环执行，从而对每个i，也就是对每个θ组成元素，
	计算Dθapprox[i]的值，我使用双边误差，也就是θ的J函数J(θ1,θ2,...,θi,...),θi调整为θi+ε,只对θi增加ε，其他项保持不变，因为使用双边
	误差，对另一边做同样的操作，只不过是θi-ε，最后得到 Dθapprox[i] = [J(θ1,θ2,...,θi+ε,...)-J(θ1,θ2,...,θi-ε,...)]/2ε
	Dθapprox[i]逼近于dθ[i]=∂J/∂θi,dθ[i]是代价函数的偏导数，然后对i的每个值都执行这个运算,最后得到两个向量，得到dθ的逼近值Dθapprox,
	dθ和Dθapprox与θ具有相同的维度，你要做的就是验证这些向量是否彼此接近。
	
	具体来说，如何定义两个向量是否真的接近彼此？
	我一般做下列运算，计算这两个向量的距离：Dθapprox-dθ的欧几里得范数(2范数)||Dθapprox-dθ||，然后用向量长度做归一化，结果为：
	||Dθapprox-dθ||/(||Dθapprox||+||dθ||),分母只是用于预防这些向量太小或者太大，分母使得这个方程式变成比率，我们实际执行这个方程式，
	ε值可能为10^-7，使用这个取值范围内的ε，如果你发现计算方程式得到的值为10^-7或更小，这就很好，这意味着导数逼近很有可能是正确的。
	如果它的值在10^-5范围内，我就要小心了，也许这个值没问题，但是我会再次检查这个向量的所有项，确保没有一项误差过大，如果有一项误差
	非常大，可能这里有bug，如果左边这个方程式的结果是10^-3,我就会担心是否存在bug，结果应该比10^-3小很多，这时应该检查所有θ项，看看
	是否有一个具体的i值使得Dθapprox与dθ大不相同，并用它来追踪一些求导计算是否正确。经过调试，最终结果应该是10^-7或更小你的实施才正确

【7】在神经网络中实施梯度检验的使用技巧和注意事项
	第1点，不要在训练中使用梯度检验，它只用于调试，我的意思是计算所有i值的Dθapprox[i]是一个非常慢的计算过程，为了实施梯度下降，你必
	须使用backprop来计算dθ，并使用backprop来计算导数，只有调试的时候，你才会计算它来确认数值是否接近dθ,完成后你会关闭梯度检验，
	每一个梯度下降的迭代过程都不再执行梯度检验，因为它太慢了。
	
	第2点，如果算法的梯度检验失败，要检查所有项，并试着找出bug。也就是说如果Dθapprox[i]和dθ的值相差很大，我们要做的就是查找不同的i
	值，看看是哪个导致Dθapprox[i]和dθ的值相差这么多。举个例子，如果你发现，相对于某些层或某层的db[l],其中θ或dθ的值相差很大，但是
	dw[l]的各项非常接近，注意，θ的各项与b和w的各项都是一一对应的，这时，你可能会发现，在计算参数b的导数db的过程中存在bug，反过来
	也一样，如果你发现他们的值相差很大，Dθapprox和dθ相差很大，你会发现所有这些项都来自dw或某层的dw,可能帮你定位bug的位置。虽然未必
	能够帮你准确定位bug的位置，但是它可以帮助你估计需要在哪些地方追踪bug。
	
	第3点，如果你使用l正则化，那么在实施梯度检验时，请注意正则项。如果代价函数J等于J(θ)=1/m *ΣL(a(i),y(i)) + λ/2m*Σ||w^[l]||F^2,
	dθ等于与θ相关的J函数的梯度，包括这个正则项，记住一定要包括这个正则项。
	
	第4点，梯度检验不能与dropout同时使用，因为每次迭代过程中，dropout会随机消除隐层单元的不同子集，难以计算dropout在梯度下降上的
	代价函数J,因此dropout可作为优化代价函数J的一种方法，但是代价函数J被定义为对所有指数极大的节点子集求和，而在任何迭代过程中，
	这些节点都可能被消除，所以很难计算代价函数J，你只是对成本函数做抽样，用dropout，每次随机消除不同的子集，，所以难用梯度检验来
	双重检验dropout的计算，所以我一般不同时使用梯度检验和dropout,如果你想这样做，可以把dropout中的keep_prob设置为1,然后打开dropout，
	并寄希望于dropout的实施是正确的。你还可以做点别的，比如修改节点丢失的模式，确认梯度检验是正确的。实际上，我一般不这么做。我建议
	关闭dropout，用梯度检验进行双重检查，在没有dropout的情况下，你的算法至少是正确的，然后打开dropout。
	
	第5点，也是比较微妙的一点，现实中几乎不会出现这种情况，当W和b接近0时，梯度下降的实施是正确的。在随机初始化过程中，但是在运行
	梯度下降时，w和b变得更大，可能只有在w和b接近0时，backprop的实施才是正确的，但是当w和b变大时，它会变得越来越不准确。你需要做一件事，
	我不经常这么做，就是在随机初始化过程中，运行梯度检验，然后再训练网络，w和b会有一段时间远离0,如果随机初始化值比较小，反复训练网络
	之后，在重新运行梯度检验。
		
		
		
		
		
		

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
		