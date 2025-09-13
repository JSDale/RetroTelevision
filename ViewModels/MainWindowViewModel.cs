using LibVLCSharp.Shared;

namespace RetroTelevision.ViewModels;

public partial class MainWindowViewModel : ViewModelBase
{
    public MediaPlayer Player { get; }

    private readonly LibVLC _vlcPlayer = new();

    public MainWindowViewModel()
    {
        Core.Initialize();
        Player = new MediaPlayer(_vlcPlayer);
    }

    public void OnLoad()
    {
        using var media = new Media(_vlcPlayer, @"", FromType.FromPath);
        Player.Play(media);
    }
}
