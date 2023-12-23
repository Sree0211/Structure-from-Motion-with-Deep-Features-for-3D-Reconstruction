// main script
// Talks about overall workflow, combining traditional SfM with deep features

#include<iostream>
#include<opencv2/opencv.hpp>

#include<deep_feature_extractor.h>
#include<keypoint_fusion.h>
#include<sfm_module.h>
#include<triangulation_bundle_adjustment.h>
#include<visualization.h>

using namespace std;
using namespace cv;

int main()
{
    //! call the deep feature extractor file
    system("deep_feature_extractor.py");

    //! Run the Structure from Motion module

    //! Combine the key points acquired

    //! Perform Triangulation to calculate the parallax

    //! Visualise the model

    return 0;

}