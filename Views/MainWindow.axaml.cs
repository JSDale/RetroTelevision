using System;
using Avalonia.Controls;
using RetroTelevision.ViewModels;

namespace RetroTelevision.Views;

public partial class MainWindow : Window
{
    private readonly MainWindowViewModel _viewModel;

    public MainWindow(MainWindowViewModel viewModel)
    {
        _viewModel = viewModel;
        InitializeComponent();
        this.Opened += OpenComplete;
    }

    private void OpenComplete(object? obj, EventArgs args)
    {
        _viewModel.OnLoad();
    }
}