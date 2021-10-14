<h1>Automated greenhouse.io Forms</h1>

<p align="center">
    <!-- code size  -->
    <img src="https://img.shields.io/github/languages/code-size/GSPuniani/automated-greenhouse-forms" />
    <!-- issues -->
    <img src="https://img.shields.io/github/issues/GSPuniani/automated-greenhouse-forms" />
    <!-- pull requests -->
    <img src="https://img.shields.io/github/issues-pr/GSPuniani/automated-greenhouse-forms" />
    <!-- number of commits per year -->
    <img src="https://img.shields.io/github/commit-activity/y/GSPuniani/automated-greenhouse-forms" />
    <!-- last commit -->
    <img src="https://img.shields.io/github/last-commit/GSPuniani/automated-greenhouse-forms" />
</p>


- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [License](#license)


## Project Overview

Many job application forms are hosted on a subdomain of greenhouse.io. However, the process of filling out forms on greenhouse.io can be unnecessarily time-consuming and tedious. Job applicants must manually type out their personal information for each application. Unfortunately, it is not possible to save this information because applicants cannot create accounts on greenhouse.io (only recruiters can). 

This project is an attempt to automate the process of filling out these greenhouse.io forms. Instructions for downloading and running the Python script are included below.



## Requirements

| Platform | Minimum Swift Version | Installation | Status |
| --- | --- | --- | --- |
| iOS 10.0+ / macOS 10.12+ / tvOS 10.0+ / watchOS 3.0+ | 5.1 | [CocoaPods](#cocoapods), [Carthage](#carthage), [Swift Package Manager](#swift-package-manager), [Manual](#manually) | Fully Tested |
| Linux | Latest Only | [Swift Package Manager](#swift-package-manager) | Building But Unsupported |
| Windows | Latest Only | [Swift Package Manager](#swift-package-manager) | Building But Unsupported |


## Installation

### CocoaPods

[CocoaPods](https://cocoapods.org) is a dependency manager for Cocoa projects. For usage and installation instructions, visit their website. To integrate Alamofire into your Xcode project using CocoaPods, specify it in your `Podfile`:

```ruby
pod 'Alamofire', '~> 5.4'
```

### Carthage

[Carthage](https://github.com/Carthage/Carthage) is a decentralized dependency manager that builds your dependencies and provides you with binary frameworks. To integrate Alamofire into your Xcode project using Carthage, specify it in your `Cartfile`:

```ogdl
github "Alamofire/Alamofire" ~> 5.4
```

### Swift Package Manager

The [Swift Package Manager](https://swift.org/package-manager/) is a tool for automating the distribution of Swift code and is integrated into the `swift` compiler. It is in early development, but Alamofire does support its use on supported platforms.

Once you have your Swift package set up, adding Alamofire as a dependency is as easy as adding it to the `dependencies` value of your `Package.swift`.

```swift
dependencies: [
    .package(url: "https://github.com/Alamofire/Alamofire.git", .upToNextMajor(from: "5.4.0"))
]
```

### Manually

If you prefer not to use any of the aforementioned dependency managers, you can integrate Alamofire into your project manually.

#### Embedded Framework

- Open up Terminal, `cd` into your top-level project directory, and run the following command "if" your project is not initialized as a git repository:

  ```bash
  $ git init
  ```

- Add Alamofire as a git [submodule](https://git-scm.com/docs/git-submodule) by running the following command:

  ```bash
  $ git submodule add https://github.com/Alamofire/Alamofire.git
  ```

- Open the new `Alamofire` folder, and drag the `Alamofire.xcodeproj` into the Project Navigator of your application's Xcode project.

    > It should appear nested underneath your application's blue project icon. Whether it is above or below all the other Xcode groups does not matter.

- Select the `Alamofire.xcodeproj` in the Project Navigator and verify the deployment target matches that of your application target.
- Next, select your application project in the Project Navigator (blue project icon) to navigate to the target configuration window and select the application target under the "Targets" heading in the sidebar.
- In the tab bar at the top of that window, open the "General" panel.
- Click on the `+` button under the "Embedded Binaries" section.
- You will see two different `Alamofire.xcodeproj` folders each with two different versions of the `Alamofire.framework` nested inside a `Products` folder.

    > It does not matter which `Products` folder you choose from, but it does matter whether you choose the top or bottom `Alamofire.framework`.

- Select the top `Alamofire.framework` for iOS and the bottom one for macOS.

    > You can verify which one you selected by inspecting the build log for your project. The build target for `Alamofire` will be listed as `Alamofire iOS`, `Alamofire macOS`, `Alamofire tvOS`, or `Alamofire watchOS`.

- And that's it!

  > The `Alamofire.framework` is automagically added as a target dependency, linked framework and embedded framework in a copy files build phase which is all you need to build on the simulator and a device.



## License

This project is released under the MIT license. 
