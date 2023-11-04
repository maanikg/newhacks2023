//
//  ContentView.swift
//  newHacks2023App
//
//  Created by Maanik Gogna on 2023-11-04.
//

import SwiftUI
import UIKit
import AVKit
import Vision

struct ContentView: View {
    var body: some View {
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundColor(.accentColor)
            Text("Hello, world!!!")
        }
        .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

//var model = handPose().model
//
//func viewDidLoad(){
//    let capSession = AVCaptureSession()
//    guard let capDevice = AVCaptureDevice.default(for: .video) else {return}
//    guard let input = try? AVCaptureDeviceInput(device: capDevice) else {return}
//    capSession.addInput(input)
//    capSession.startRunning()
//    let previewLayer = AVCaptureVideoPreviewLayer(session: capSession)
//    view.layer.addSublayer(previewLayer)
//    previewLayer.frame = view.frame
//}
