//
//  ToneModel.swift
//  SpeechImprovement
//
//  Created by Maanik Gogna on 2023-05-24.
//

import Foundation
import AVFoundation
import CoreML
import SoundAnalysis

let defaultConfig = MLModelConfiguration()
//let toneClassifier = try! toneModel(configuration: defaultConfig)
//let toneClassifier = try! SpeechImprovement_ML_10(configuration: defaultConfig)
//let toneClassifier = try! SpeechImprovement_ML_13(configuration: defaultConfig)
//let toneClassifier = try! SpeechImprovement_ML_14(configuration: defaultConfig)

//SpeechImprovement_ML_12 model has 100% training, 93% accuracy (25 iterations, 5.0 sec window duration, 75% window overlap)
let poseClassifier = try! handPose(configuration: defaultConfig)
//let speedClassifier = try! speedModel(configuration: defaultConfig)
//let volumeClassifier try! volumeModel(configuration: defaultConfig)
//let clarityClassifier try! clarityModel(configuration: defaultConfig)
//let classifyToneSoundReq = try! SNClassifySoundRequest(mlModel: toneClassifier.model)
let classifyToneSoundReq1 = try! SNClassifySoundRequest(mlModel: poseClassifier.model)

//let imageClassifierWrapper = try? AnimalClassifier(configuration: defaultConfig)
//let resultsObserver = ResultsObserver()
let toneOrder: [String:Int] = ["Perfect": 5, "Slightly Monotone": 4, "Monotone": 3, "More Monotone": 2, "Most Monotone": 1, "Background": 0]
let toneOrderReverse: [Int:String] = [5: "Perfect", 4: "Slightly Monotone", 3: "Monotone", 2: "More Monotone", 1: "Most Monotone", 0: "Background"]

//OVERLAPPING INTERVALS MEANS IT DOESNT ADD UP TO DURATION

//TODO: COMMENTED OUT PRINTING FOR CLARITY
/// An observer that receives results from a classify sound request.
class ResultsObserver: NSObject, SNResultsObserving {
    var resultDict: [String:[String:Double]] = [:]
    var totalTime:Double = 0
    var totalAnalysisTime:Double = 0
    var analysisSuccess:Bool = false
    
    //    let toneOrder: [String:Int] = []
    //    let speedOrder: [String:Int] = []
    //    let volumeOrder: [String:Int] = []
    //MARK: SORTING CLOTURES
    //    for (tempVar, _) in resultDict{
    //        print()
    //        resultDict[key] = resultDict[key]?.sorted(by: {toneOrder[$0.key]<toneOrder[$0.key]})
    //    }
    //    let sortedTone = resultDict.keys.sorted{(key1, key2) -> Bool in
    //        return toneOrder[key1] < toneOrder[key2]
    //    }
    
    /// Notifies the observer when a request generates a prediction.
    func request(_ request: SNRequest, didProduce result: SNResult) {
        // Downcast the result to a classification result.
        guard let result = result as? SNClassificationResult else  { return }
        
        // Get the prediction with the highest confidence.
        //        guard let classification = result.classifications.first else { return }
        let classification = result.classifications
        // Get the starting time.
        let timeInSeconds = result.timeRange.start.seconds
        let endTime = result.timeRange.end.seconds
        
        // Convert the time to a human-readable string.
        let formattedTime = String(format: "%.2f", timeInSeconds)
        //COMMENTED OUT
        print("Analysis result for audio at time: \(formattedTime) - \(String(format:"%.2f", endTime))")
        totalAnalysisTime+=(endTime-timeInSeconds)
        
        for classif in classification{
            let percent = classif.confidence * 100.0
            let percentString = String(format: "%.2f%%", percent)
            let modelName = classif.identifier.components(separatedBy: " ").first!.trimmingCharacters(in: .whitespaces)
            let categoryLabel = classif.identifier.components(separatedBy: " ").dropFirst().joined(separator: " ")
            
            if resultDict[modelName] == nil{
                resultDict[modelName] = [:]
            }
            //            if let value = resultDict[classif.identifier]{
            //                resultDict[classif.identifier] = value + classif.confidence*result.timeRange.duration.seconds
            //            }
            //            else{
            //                resultDict[classif.identifier] = classif.confidence*result.timeRange.duration.seconds
            //            }
            if let value = resultDict[modelName]![categoryLabel]{
                resultDict[modelName]![categoryLabel] = value + classif.confidence*result.timeRange.duration.seconds
            }
            else{
                resultDict[modelName]![categoryLabel] = classif.confidence*result.timeRange.duration.seconds
            }
            
            //COMMENTED OUT
            if (round(percent) != 0){
                print("\(classif.identifier): \(percentString) confidence.")
            }
        }
        
        // Convert the confidence to a percentage string.
        //        let percent = classification.confidence * 100.0
        //        let percentString = String(format: "%.2f%%", percent)
        
        // Print the classification's name (label) with its confidence.
        //        print("\(classification.identifier): \(percentString) confidence.\n")
    }
    
    /// Notifies the observer when a request generates an error.
    func request(_ request: SNRequest, didFailWithError error: Error) {
        print("The analysis failed: \(error.localizedDescription)")
    }
    
    /// Notifies the observer when a request is complete.
    func requestDidComplete(_ request: SNRequest) {
        print("The sound classifier request completed successfully!")
        analysisSuccess = true
        print(resultDict)
        //sort the keys in each inner dictionary of resultDict by the values
//        for (key, _) in resultDict{
//            let sortedInnerDict = resultDict[key]!.sorted { (entry1, entry2) in
//                entry1.value < entry2.value
//            }
//            resultDict[key] = Dictionary(uniqueKeysWithValues: sortedInnerDict)
//        }
//        print(resultDict)
    }
}

/// Creates an analyzer for an audio file.
/// - Parameter audioFileURL: The URL to an audio file.
func createAnalyzer(audioFileURL: URL) -> SNAudioFileAnalyzer? {
    return try? SNAudioFileAnalyzer(url: audioFileURL)
}
