# DataAnalytics
## 0 - Code and description

### Code
https://github.com/Juan-Ignacio-Ortega/DataAnalytics/blob/main/DataAnalyticsCode_JIOG.py

### Description
https://github.com/Juan-Ignacio-Ortega/DataAnalytics/blob/main/DataAnalyticsDescription_JIOG.ipynb

## 1 - Introduction

In the world, we are increasingly overwhelmed by data. With data on each of the devices we handle daily, data within the web and the cloud. As this information increases, so do the opportunities to gain insights from the data. It's not just about looking at the data, it's about what it can tell us about who or what is generating it.
Today we can find information on data analysis techniques, knowledge that will allow us not only to obtain opportunities to take advantage of data, but also to know the best ways to generate information and use it.
Finally, it is recommended to have an approach towards data analysis techniques, which begins with this writing. [1]
In this report, you can find generalized algorithms for use with any database to extract its first features for analysis. In addition, to find a couple of corrective techniques that will help improve the database that is entered.

## 2 - Methodology

STATISTICAL DEFINITIONS

• The sample mean (Average)
Indicates the center of the data.
Average = (1 / n) * sum of Xi [2]
• Deviations ((X1 - Xaverage), . . . , (Xn - Xaverage)) Distances of each sample value from the sample mean. Being a subtraction, it generates both positive and negative values, so it is squared when used in the variance and standard deviation, to make all subtraction results positive.
• Sample variance This is the average of the squared deviations, except that we divide it by n-1 instead of n.
s2 = (1 / (n - 1)) * sum of ((Xi - Xaverage)2) [2]
• Standard deviation Measures the degree of dispersion.
s = (s2)1 / 2 or square root of s2 [2]
• Quartiles
The median divides the sample in half, the quartiles divide it, as much as possible, into fourths.
First quartile = 0.25 (n + 1) [2]
Second quartile = 0.5 (n + 1) [2] –> Identical to the median
Third quartile = 0.75 (n + 1) [2]
The result tells you the number of the value that represents the X quartile, of the data ordered in ascending order.
Only if the result is an integer, otherwise the average of the sample values ​​on either side of this value is taken, sampling in ascending order.
• Covariance
It is a measure of the strength of the relationship between two random variables [2].
cov(X, Y) = average((Xi - average of X) * (Yi - average of Y)) [2]

CONCEPTS IN DATA MANAGEMENT

• Instances
Each instance is characterized by the values ​​of the attributes that measure different aspects for each measurement. If we see it in the sense of a database, the instances would be the records of this, that is, the rows.
• Attributes
If we see it as a database, the attributes would be the equivalent of the columns. The value of an attribute for a particular instance is the measure of the quantity to which the attribute refers.
• Attribute classification

-Categorical attribute:
Categorical (qualitative): represent categories rather than numbers. They are further divided into:
Nominal: they have no significant order.
Ordinals: they have a definite order.

-Number attribute:
Numerical (quantitative): they are attributes that are numbers, they are divided in turn into:
Interval: there is no .
Rate: zero exists.
Discrete attribute: Has a finite or countable number of values.
Continuous attribute: It has an infinite number of possible values.

• Types of distribution according to histograms
Uniform Histogram
Normal Histogram (Unimodal)
Left skewed Unimodal Histogram
Right skewed Unimodal Histogram
Multimodal Histogram
exponential histogram
• Data quality problem any unusual data found in the database.
The most common data problems are:
Missing values.
Irregular cardinality problems. It occurs when a feature has data that is not what would be expected from a feature.

Outliers outliers.
Values ​​that are located very far from the central tendency of a characteristic. It can be categorized into valid and invalid [1].

• Balance between classes
It seeks to have the same number of examples for each class.
• Normalize the data
Some AI algorithms require all data to be centered in a specific range of values, typically -1 to 1 or 0 to 1. Even if data is not required to be within values, it is generally a good idea to make sure the values ​​are within a specific range.

Normalization of ordinal values
To normalize an ordinal set, you have to preserve the order.

Normalization of quantitative values
The first thing you have to do is observe the range in which these values ​​are found and the interval to which you want to normalize. Not all values ​​need to be normalized.

It is necessary to perform the calculations of the following variables to find the normalized value:
-Maximum of the data = the highest value of the observation without normalizing [1].
-Minimum of the data = the smallest height of the observation without normalizing [1].
-Maximum normalized = the highest bound value to which the maximum of the data will be normalized [1].
-Minimum normalized = the lowest bounding value to which the minimum of the data will be normalized [1].
-Data range = Maximum of the data - Minimum of the data [1].
-Normalized range = Normalized maximum - Normalized minimum [1].
-D = Value to normalize - Minimum of the data [1].
-DPct = D / Data range [1].
-dNorm = Normalized Range * DPct [1].
-Normalized = Minimum normalized + dNorm [1].

In this way, the normalized value is obtained.
• Data imputation

In data science, there are usually two approaches to dealing with these missing values:
omit instances with missing values ​​or perform imputation techniques and estimate missing data using existing values.

Imputation is a technique for replacing missing values ​​with values ​​that are found. The objective is to have a database with the least amount of missing instances that contain the same distribution as the existing data so that they can be analyzed.
Deterministic imputation techniques They work when, according to the same conditions of the data, they produce the same answers. Among these techniques is imputation by
nearest neighbor.
Imputation by nearest neighbor: The distance between the instance to be imputed is calculated, usually by means of the Euclidean distance and the data that has an established value. Once the closest data is calculated, it is used to impute the missing instance.

• Euclidean distance

The Euclidean distance is based on the two-dimensional distance between two vectors. That is, the distance between two points as if a line were drawn with a ruler from one point to another. Specifically, if there are two points (x1, y1) and (x2, y2), the Euclidean distance can be calculated using the equation [1]:

d = square root((x2 - x1)ˆ2 + (y2 - y1)ˆ2) [1]

## 3 - References

[1] M. A. Aceves Fernández, Inteligencia Artificial para programadores con prisa. UNIVERSO de
LETRAS, 2021.

[2] W. Navidi, Estadística para ingenieros. México: Mc Graw Hill, 2006.
