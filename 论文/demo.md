# demo

<style>
    #part1 {
    width: 300px;
    height: 300px;
    float: left;
    }
    #part2 {
    width: 300px;
    height: 300px;
    float: left;
    }
    #part3 {
    width: 300px;
    height: 300px;
    float: left;
    clear: left;
    }
    #part4 {
    width: 300px;
    height: 300px;
    float: left;
    }
</style>

## 0. 引言
初值敏感性是衡量混沌系统的一个重要属性，即系统的初始值发生细微的变化，其输出结果会产生巨大的差异。李雅普诺夫指数(Lyaponuv exponents)常常被用来判定一个系统的混沌性，通过图像可以直观地看出某个系统或者映射是否是混沌系统或映射。
Lyaponuv 指数表示相空间相邻轨迹的平均指数发散率的数值特征。又称李雅普诺夫特征指数，是用于识别混沌运动若干数值的特征之一。初值敏感性是衡量混沌系统的一个重要属性，即系统的初始值发生细微的变化，其输出结果会产生巨大的差异。李雅普诺夫指数(Lyaponuv exponents)常常被用来判定一个系统的混沌性，通过图像可以直观地看出某个系统或者映射是否是混沌系统或映射。
Lyaponuv 指数表示相空间相邻轨迹的平均指数发散率的数值特征。又称李雅普诺夫特征指数，是用于识别混沌运动若干数值的特征之一。初值敏感性是衡量混沌系统的一个重要属性，即系统的初始值发生细微的变化，其输出结果会产生巨大的差异。李雅普诺夫指数(Lyaponuv exponents)常常被用来判定一个系统的混沌性，通过图像可以直观地看出某个系统或者映射是否是混沌系统或映射。
Lyaponuv 指数表示相空间相邻轨迹的平均指数发散率的数值特征。又称李雅普诺夫特征指数，是用于识别混沌运动若干数值的特征之一。初值敏感性是衡量混沌系统的一个重要属性，即系统的初始值发生细微的变化，其输出结果会产生巨大的差异。李雅普诺夫指数(Lyaponuv exponents)常常被用来判定一个系统的混沌性，通过图像可以直观地看出某个系统或者映射是否是混沌系统或映射。
Lyaponuv 指数表示相空间相邻轨迹的平均指数发散率的数值特征。又称李雅普诺夫特征指数，是用于识别混沌运动若干数值的特征之一。

## 1. 提出混沌映射

### 1.1 经典的混沌映射

#### 1.1.1 Logistic 映射
Logistic 映射是一个二次多项式映射，经常作为典型范例来说明复杂的混沌现象是如何从非常简单的非线性动力学方程中产生的。它的数学表达式为：
$$x_{n+1} = \mu x_n(1-x_n), \mu \in [0,4], x_n \in (0, 1) \tag{1}$$
上式(1)中，$\mu$ 被称为分支参数。Logistic 映射的状态与 $\mu$ 的取值有关，当$3.5699456 < \mu \leq 4$ 时，系统处于混沌状态，且$\mu \approx 4$时，Logistic 映射分布最大。取$x_0 = 0.5$，分叉图如图1所示

<center>
    <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="./FILES/demo.md/37c36831.png" height=300> <br/><div style="border-bottom: 1px solid #d9d9d9; display: inline-block;">图1 Logistic 映射分叉图</div>
</center>


#### 1.1.2 Sine 映射

Sine 映射是一种以正弦函数为基础的混沌映射，它的数学表达式为：
$$x_{n+1} = \mu sin(\pi x_n), x_n \in [0, 1], \mu \in [0, 4] \tag{2}$$
上式(2)中，当 $\mu \in [3.48, 4]$ 时，系统处于混沌状态，且当 $\mu \approx 4$ 时，Sine 映射分布最大。取$x_0 = 0.5$，分叉图如图2所示

<center>
    <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="./FILES/demo.md/d37d24a3.png" height=300> <br/><div style="border-bottom: 1px solid #d9d9d9; display: inline-block;">图2 Sine 映射分叉图</div>
</center>

### 1.2 改进的混沌映射
考虑到经典的 Logistic 映射和 Sine 映射都存在分布不均匀，分支参数范围小等缺陷，本文结合这两种经典的一位混沌映射提出一种新的混沌系统——(todo: fill it)，其表达式为：
$$x_{n+1} = (t * arcsin(4 * x * (1-x))) \quad mod \quad 1, \tag{3}  x_n \in (0, 1), t \in [1, +\infty) $$
上式(3)中，$t$ 为分支参数，且 t 越大，系统混沌性表现的越明显。取$x_0 = 0.5$，当 $t=1 / t=7 / t=26$时的分支图如图3所示：

<center>
<center id="part1">
    <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="./FILES/demo.md/df4c9aa7.png" height=300> <br/><div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">(a) t=1时分支图</div>
    </center>
<center id="part2">
    <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="./FILES/demo.md/facfee94.png" height=300> <br/><div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">(b) t=7时分支图</div>
</center>
<center id="part3">
    <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="./FILES/demo.md/38d52775.png" height=300> <br/><div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">(c) t=26时分支图</div>
</center>
<center id="part4">
</center>

<br/><div style="border-bottom: 1px solid #d9d9d9; display: inline-block;">图3 xxx映射分叉图</div>
</center>

![Img](./FILES/demo.md/4b5ea90a.png)


### 1.3 性能测试

#### 1.3.1 初值敏感性
初值敏感性是衡量混沌系统的一个重要属性，即系统的初始值发生细微的变化，其输出结果会产生巨大的差异。李雅普诺夫指数(Lyaponuv exponents)常常被用来判定一个系统的混沌性，通过图像可以直观地看出某个系统或者映射是否是混沌系统或映射。
Lyaponuv 指数表示相空间相邻轨迹的平均指数发散率的数值特征。又称李雅普诺夫特征指数，是用于识别混沌运动若干数值的特征之一。
LE指数不同的取值有不同的含义：
1. 当 $LE > 0$ 时，系统进入混沌状态，存在混沌行为，对应的映射叫做混沌映射，且其混沌性强弱与LE指数的大小有关。
2. 当 $LE = 0$ 时，系统处于稳定状态。
3. 当 $LE < 0$ 时，系统的运动状态会趋于稳定且此时初值不敏感。

图4(a) 为 Sine 映射的 LE 指数图，当$\mu > 3.464$ 时，$LE > 0$；图4(b) 为 Logistic 映射的 LE 指数图，当$\mu > 3.57$ 时， $LE > 0$；图4(c) 为xxx映射的 LE 指数图，当 $t > 1$ 时，$LE>0$。

<center>
<center id="part1">
    <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="./FILES/demo.md/881238b1.png" height=300> <br/><div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">(a) Sine 映射 LE 指数图</div>
</center>
<center id="part2">
    <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="./FILES/demo.md/25531da3.png" height=300> <br/><div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">(b) Logistic 映射 LE 指数图</div>
</center>
<center  id="part3">
    <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="./FILES/demo.md/9eec7d91.png" height=300> <br/><div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">(c) t=26时分支图</div>
</center>
<center id="part4">
</center>

<br/><div style="border-bottom: 1px solid #d9d9d9; display: inline-block;">图4 LE 指数对比</div>
</center>

<br/>


## 2. 加密算法设计

### 2.1 密钥生成
设 $K$ 表示密钥，$K = \left\{ x_0, t_0, r_0, x_1, t_1, r_1, x_2, t_2, r_2 \right\}$，其中 $x, t, r$ 分别为混沌映射初始值、控制参数、迭代起步点。

$\left\{ x_i, t_i, r_i\right\}$ 分别作为xxx映射系统，即表达式(3)的初始值以及其控制参数，迭代 $r_i + M \times N$次，为了避免暂态效应，舍去前 $r_i$ 项，得到长度为 $M \times N$ 的矩阵，记作$\left\{ x_i\right\}$，$i=1,2,3$。将 $x_0$ 记作排序矩阵 $sort\_list$，$x_1$ 记作异或矩阵 $xor\_list$，$x_2$ 记作扩散矩阵 $spread\_list$。
$$
sort\_list = xxx(x_0, t_0, r_0 + M \times N) - xxx(x_0, t_0, r_0) \tag{4} \\
$$
<br/>

$$
xor\_list = xxx(x_1, t_1, r_1 + M \times N) - xxx(x_1, t_1, r_1) \tag{5} \\
$$
<br/>

$$
spread\_list = xxx(x_2, t_2, r_2 + M \times N) - xxx(x_2, t_2, r_2) \tag{6}
$$

### 2.2 加密过程
将明文图像用矩阵 $P$ 表示，其大小为 $M \times N$，利用生成的 $sort\_list, xor\_list, spread\_list$ 对原始的明文矩阵进行加密。
加密过程分为两部分——置乱和扩散。
在置乱环节，首先对 明文图像 $P$使用 $sort\_list$ 进行排序置乱，将排序置乱后的矩阵 $sorted\_list$ 与 $xor\_list$ 进行异或置乱，得到置乱完毕的矩阵 $xored\_list$。
在扩散环节，对 $xored\_list$ 使用 $spread\_list$ 进行扩散，输出最终的矩阵 $encrypted\_list$，并将矩阵作为图像输出。

具体流程图如 图5 所示
<center>
<img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="./FILES/demo.md/103a4467.png" height=450> <br/><div style="border-bottom: 1px solid #d9d9d9; display: inline-block;">图5 加密流程图</div>
</center>

#### 2.2.1 置乱过程

**Step 1:** 将 $sort\_list$ 按照先行后列的顺序，变换大小为 $M \times N$ 的矩阵$new\_sort\_list$。
**Step 2：** 计算 $new\_sort\_list$ 每一行的和 $\left\{ row\_sum_i\right\}(i=1,2...N)$，根据$\left\{ row\_sum_i \right\}$对行索引进行降序排序，得到一个长度 $N$ 的矩阵 $\left\{ row_i\right\}(i=1,2...N)$。根据每一行的前后位置变化，对原始图像 $P$ 进行重组，得到 $row\_sorted\_list$。
**Step 3:** 计算 $new\_sort\_list$ 每一列的和 $\left\{ col\_sum_i \right\}(i=1,2...M)$，根据$\left\{ col\_sum_i \right\}$对列索引进行降序排序，得到一个长度 $M$ 的矩阵 $\left\{col_i \right\}(i=1,2....M)$。$\left\{col_i \right\}$ 对经过 Step 1 排序后的矩阵$row\_sorted\_list$再一次重组，得到最终排序完毕的矩阵 $sorted\_list$。

置换图如图6所示，根据$new\_sort\_list$对原始图像 $P$ 矩阵的对应关系进行置换形成置换后的二维矩阵 $sorted\_list$

<center>
<img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="./FILES/demo.md/7ff8a3c8.png" height=450> <br/><div style="border-bottom: 1px solid #d9d9d9; display: inline-block;">图6 排序置乱过程</div>
</center>

**Step4:** 将得到的 $sorted\_list$ 和 $xor\_list$ 进行异或，得到置乱完毕的矩阵 $xored\_list$

#### 2.2.2 扩散过程

**Step1:** 借助xxx混沌映射系统得到的 $spread\_list$ 根据式(7)和式(8)给出的计算规则对明文图像第一行的所有像素值进行变换，即将 P(1,j) 转化为 E(1,j)

$$
E(1,1) = ( P(1,1) + spread\_list(1,1) )\quad mod \quad 255 \tag{7}
$$
$$
E(1,j) = ( P(1,j) + spread\_list(1,j) + E(1, j-1) ) \quad mod \quad 255 \tag{8}
$$

**Step2:** 借助xxx混沌映射系统得到的 $spread\_list$ 根据式(9)给出的计算规则对明文图像第一列所有的像素值进行变换，即将 P(i,1) 转化为 E(i,1)

$$
E(i,1) = ( P(i,1) + spread\_list(i,1) + E(i-1,1) ) \quad mod \quad 255 \tag{9}
$$

**Step3:** 借助xxx混沌映射系统得到的 $spread\_list$ 根据式(10)给出的计算规则对明文图像其他的灰度值进行变换，即将 P(i,j) 转化为 E(i,j)

$$
E(i,j) = ( P(i,j) + spread\_list(i,j) + E(i-1,j) + E(i,j-1) ) \quad mod \quad 255 \\
\tag{10}
$$
<br/>
完成上述扩散步骤后，得到的矩阵 $E$ 即加密完毕的矩阵 $encrypted\_list$，也即加密后图像的灰度矩阵。

## 3. 仿真实验及相关分析
本节所做实验、分析均在 macOS Monterey 操作系统、 Apple M1 Pro 芯片， python3.8 环境下进行。
### 3.1 仿真实验结果
以尺寸为 $256 \times 256$的 Lena 图像 
作为示例，测试本文算法的相关性能，其明文图像和密文图像以及解密图像如图7所示。

<center>
<center id="part1">
    <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="./FILES/demo.md/5b63f754.png" height=300><br/><div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">(a) 原始图像</div>
</center>
<center id="part2">
    <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="./FILES/demo.md/5c026da6.png" height=300> <br/><div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">(b) 加密后的密文图片</div>
</center>
<center  id="part3">
    <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="./FILES/demo.md/5b63f754.png" height=300> <br/><div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">(c) 解密后的图片</div>
</center>
<center  id="part4">
</center>

<br/><div style="border-bottom: 1px solid #d9d9d9; display: inline-block;">图7 仿真实验结果</div>
</center>


### 3.2 密钥空间分析
xxx混沌映射系统的密钥 $K = \left\{ x_0, t_0, r_0, x_1, t_1, r_1, x_2, t_2, r_2 \right\}$，内含包括三对 $x,t,r$ 变量，其中 $x \in (0, 1)$ 和 $t \in (1, +\infty)$ 的理论密钥空间均为无限，考虑到浮点数计算问题，实际建议使用$x$的取值精度为$10^{-10}$，考虑到计算时间问题，迭代次数 $r$ 的取值暂定为 $(0, 10^{6})$。综上所述，所提出的加密算法能够非常有效的抵抗暴力穷举攻击。

### 3.3 直方图分析
加密后的图像会受到统计攻击。攻击者收集在密文图像中每个像素出现的频率，提取出相关信息，来检查一个看似有噪声的图像是否携带了有价值的信息。所以一个性能良好的加密算法，在图像被加密完毕后每个像素出现的次数、频率应该是均匀的。

直方图是反映数字图像中像素灰度值出现频率的统计图，是最直观的方法之一，它可以直观的体现出各个像素的分布。图8为加密前后图像的直方图。

<center>
<center id="part1">
    <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="./FILES/demo.md/5b63f754.png" height=300> <br/><div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">(a) 原始图像</div>
</center>
<center id="part2">
    <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="./FILES/demo.md/5c026da6.png" height=300> <br/><div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">(b) 加密后的密文图片</div>
</center>
<center  id="part3">
    <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="./FILES/demo.md/5b63f754.png" height=300> <br/><div style="color:orange; border-bottom: 1px solid #d9d9d9; display: inline-block; color: #999; padding: 2px;">(c) 解密后的图片</div>
</center>
<center  id="part4">
</center>

<br/><div style="border-bottom: 1px solid #d9d9d9; display: inline-block;">图7 仿真实验结果</div>
</center>


