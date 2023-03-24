#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : gnome-text-editor
Version  : 44.0
Release  : 10
URL      : https://download.gnome.org/sources/gnome-text-editor/44/gnome-text-editor-44.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-text-editor/44/gnome-text-editor-44.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: gnome-text-editor-bin = %{version}-%{release}
Requires: gnome-text-editor-data = %{version}-%{release}
Requires: gnome-text-editor-license = %{version}-%{release}
Requires: gnome-text-editor-locales = %{version}-%{release}
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(editorconfig)
BuildRequires : pkgconfig(enchant-2)
BuildRequires : pkgconfig(gtksourceview-5)
BuildRequires : pkgconfig(libadwaita-1)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# GNOME Text Editor
Text Editor is a simple text editor that focuses on session management.
It works hard to keep track of changes and state even if you quit the application.
You can come back to your work even if you've never saved it to a file.

%package bin
Summary: bin components for the gnome-text-editor package.
Group: Binaries
Requires: gnome-text-editor-data = %{version}-%{release}
Requires: gnome-text-editor-license = %{version}-%{release}

%description bin
bin components for the gnome-text-editor package.


%package data
Summary: data components for the gnome-text-editor package.
Group: Data

%description data
data components for the gnome-text-editor package.


%package doc
Summary: doc components for the gnome-text-editor package.
Group: Documentation

%description doc
doc components for the gnome-text-editor package.


%package license
Summary: license components for the gnome-text-editor package.
Group: Default

%description license
license components for the gnome-text-editor package.


%package locales
Summary: locales components for the gnome-text-editor package.
Group: Default

%description locales
locales components for the gnome-text-editor package.


%prep
%setup -q -n gnome-text-editor-44.0
cd %{_builddir}/gnome-text-editor-44.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679692159
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-text-editor
cp %{_builddir}/gnome-text-editor-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-text-editor/338650eb7a42dd9bc1f1c6961420f2633b24932d || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-text-editor

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-text-editor

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.TextEditor.desktop
/usr/share/dbus-1/services/org.gnome.TextEditor.service
/usr/share/glib-2.0/schemas/org.gnome.TextEditor.gschema.xml
/usr/share/gnome-text-editor/styles/builder-dark.xml
/usr/share/gnome-text-editor/styles/builder.xml
/usr/share/gnome-text-editor/styles/peninsula-dark.xml
/usr/share/gnome-text-editor/styles/peninsula.xml
/usr/share/gnome-text-editor/styles/printing.xml
/usr/share/icons/hicolor/scalable/apps/org.gnome.TextEditor.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.TextEditor-symbolic.svg
/usr/share/metainfo/org.gnome.TextEditor.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/gnome-text-editor/basics-create-new-file.page
/usr/share/help/C/gnome-text-editor/basics-draft-folder.page
/usr/share/help/C/gnome-text-editor/basics-open-file.page
/usr/share/help/C/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/C/gnome-text-editor/edit-undo-redo.page
/usr/share/help/C/gnome-text-editor/index.page
/usr/share/help/C/gnome-text-editor/legal.xml
/usr/share/help/C/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/C/gnome-text-editor/media/search-recent.png
/usr/share/help/ca/gnome-text-editor/basics-create-new-file.page
/usr/share/help/ca/gnome-text-editor/basics-draft-folder.page
/usr/share/help/ca/gnome-text-editor/basics-open-file.page
/usr/share/help/ca/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/ca/gnome-text-editor/edit-undo-redo.page
/usr/share/help/ca/gnome-text-editor/index.page
/usr/share/help/ca/gnome-text-editor/legal.xml
/usr/share/help/ca/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/ca/gnome-text-editor/media/search-recent.png
/usr/share/help/cs/gnome-text-editor/basics-create-new-file.page
/usr/share/help/cs/gnome-text-editor/basics-draft-folder.page
/usr/share/help/cs/gnome-text-editor/basics-open-file.page
/usr/share/help/cs/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/cs/gnome-text-editor/edit-undo-redo.page
/usr/share/help/cs/gnome-text-editor/index.page
/usr/share/help/cs/gnome-text-editor/legal.xml
/usr/share/help/cs/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/cs/gnome-text-editor/media/search-recent.png
/usr/share/help/da/gnome-text-editor/basics-create-new-file.page
/usr/share/help/da/gnome-text-editor/basics-draft-folder.page
/usr/share/help/da/gnome-text-editor/basics-open-file.page
/usr/share/help/da/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/da/gnome-text-editor/edit-undo-redo.page
/usr/share/help/da/gnome-text-editor/index.page
/usr/share/help/da/gnome-text-editor/legal.xml
/usr/share/help/da/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/da/gnome-text-editor/media/search-recent.png
/usr/share/help/de/gnome-text-editor/basics-create-new-file.page
/usr/share/help/de/gnome-text-editor/basics-draft-folder.page
/usr/share/help/de/gnome-text-editor/basics-open-file.page
/usr/share/help/de/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/de/gnome-text-editor/edit-undo-redo.page
/usr/share/help/de/gnome-text-editor/index.page
/usr/share/help/de/gnome-text-editor/legal.xml
/usr/share/help/de/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/de/gnome-text-editor/media/search-recent.png
/usr/share/help/es/gnome-text-editor/basics-create-new-file.page
/usr/share/help/es/gnome-text-editor/basics-draft-folder.page
/usr/share/help/es/gnome-text-editor/basics-open-file.page
/usr/share/help/es/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/es/gnome-text-editor/edit-undo-redo.page
/usr/share/help/es/gnome-text-editor/index.page
/usr/share/help/es/gnome-text-editor/legal.xml
/usr/share/help/es/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/es/gnome-text-editor/media/search-recent.png
/usr/share/help/eu/gnome-text-editor/basics-create-new-file.page
/usr/share/help/eu/gnome-text-editor/basics-draft-folder.page
/usr/share/help/eu/gnome-text-editor/basics-open-file.page
/usr/share/help/eu/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/eu/gnome-text-editor/edit-undo-redo.page
/usr/share/help/eu/gnome-text-editor/index.page
/usr/share/help/eu/gnome-text-editor/legal.xml
/usr/share/help/eu/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/eu/gnome-text-editor/media/search-recent.png
/usr/share/help/fr/gnome-text-editor/basics-create-new-file.page
/usr/share/help/fr/gnome-text-editor/basics-draft-folder.page
/usr/share/help/fr/gnome-text-editor/basics-open-file.page
/usr/share/help/fr/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/fr/gnome-text-editor/edit-undo-redo.page
/usr/share/help/fr/gnome-text-editor/index.page
/usr/share/help/fr/gnome-text-editor/legal.xml
/usr/share/help/fr/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/fr/gnome-text-editor/media/search-recent.png
/usr/share/help/gl/gnome-text-editor/basics-create-new-file.page
/usr/share/help/gl/gnome-text-editor/basics-draft-folder.page
/usr/share/help/gl/gnome-text-editor/basics-open-file.page
/usr/share/help/gl/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/gl/gnome-text-editor/edit-undo-redo.page
/usr/share/help/gl/gnome-text-editor/index.page
/usr/share/help/gl/gnome-text-editor/legal.xml
/usr/share/help/gl/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/gl/gnome-text-editor/media/search-recent.png
/usr/share/help/hu/gnome-text-editor/basics-create-new-file.page
/usr/share/help/hu/gnome-text-editor/basics-draft-folder.page
/usr/share/help/hu/gnome-text-editor/basics-open-file.page
/usr/share/help/hu/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/hu/gnome-text-editor/edit-undo-redo.page
/usr/share/help/hu/gnome-text-editor/index.page
/usr/share/help/hu/gnome-text-editor/legal.xml
/usr/share/help/hu/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/hu/gnome-text-editor/media/search-recent.png
/usr/share/help/id/gnome-text-editor/basics-create-new-file.page
/usr/share/help/id/gnome-text-editor/basics-draft-folder.page
/usr/share/help/id/gnome-text-editor/basics-open-file.page
/usr/share/help/id/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/id/gnome-text-editor/edit-undo-redo.page
/usr/share/help/id/gnome-text-editor/index.page
/usr/share/help/id/gnome-text-editor/legal.xml
/usr/share/help/id/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/id/gnome-text-editor/media/search-recent.png
/usr/share/help/it/gnome-text-editor/basics-create-new-file.page
/usr/share/help/it/gnome-text-editor/basics-draft-folder.page
/usr/share/help/it/gnome-text-editor/basics-open-file.page
/usr/share/help/it/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/it/gnome-text-editor/edit-undo-redo.page
/usr/share/help/it/gnome-text-editor/index.page
/usr/share/help/it/gnome-text-editor/legal.xml
/usr/share/help/it/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/it/gnome-text-editor/media/search-recent.png
/usr/share/help/ko/gnome-text-editor/basics-create-new-file.page
/usr/share/help/ko/gnome-text-editor/basics-draft-folder.page
/usr/share/help/ko/gnome-text-editor/basics-open-file.page
/usr/share/help/ko/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/ko/gnome-text-editor/edit-undo-redo.page
/usr/share/help/ko/gnome-text-editor/index.page
/usr/share/help/ko/gnome-text-editor/legal.xml
/usr/share/help/ko/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/ko/gnome-text-editor/media/search-recent.png
/usr/share/help/ne/gnome-text-editor/basics-create-new-file.page
/usr/share/help/ne/gnome-text-editor/basics-draft-folder.page
/usr/share/help/ne/gnome-text-editor/basics-open-file.page
/usr/share/help/ne/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/ne/gnome-text-editor/edit-undo-redo.page
/usr/share/help/ne/gnome-text-editor/index.page
/usr/share/help/ne/gnome-text-editor/legal.xml
/usr/share/help/ne/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/ne/gnome-text-editor/media/search-recent.png
/usr/share/help/nl/gnome-text-editor/basics-create-new-file.page
/usr/share/help/nl/gnome-text-editor/basics-draft-folder.page
/usr/share/help/nl/gnome-text-editor/basics-open-file.page
/usr/share/help/nl/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/nl/gnome-text-editor/edit-undo-redo.page
/usr/share/help/nl/gnome-text-editor/index.page
/usr/share/help/nl/gnome-text-editor/legal.xml
/usr/share/help/nl/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/nl/gnome-text-editor/media/search-recent.png
/usr/share/help/pl/gnome-text-editor/basics-create-new-file.page
/usr/share/help/pl/gnome-text-editor/basics-draft-folder.page
/usr/share/help/pl/gnome-text-editor/basics-open-file.page
/usr/share/help/pl/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/pl/gnome-text-editor/edit-undo-redo.page
/usr/share/help/pl/gnome-text-editor/index.page
/usr/share/help/pl/gnome-text-editor/legal.xml
/usr/share/help/pl/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/pl/gnome-text-editor/media/search-recent.png
/usr/share/help/pt_BR/gnome-text-editor/basics-create-new-file.page
/usr/share/help/pt_BR/gnome-text-editor/basics-draft-folder.page
/usr/share/help/pt_BR/gnome-text-editor/basics-open-file.page
/usr/share/help/pt_BR/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/pt_BR/gnome-text-editor/edit-undo-redo.page
/usr/share/help/pt_BR/gnome-text-editor/index.page
/usr/share/help/pt_BR/gnome-text-editor/legal.xml
/usr/share/help/pt_BR/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/pt_BR/gnome-text-editor/media/search-recent.png
/usr/share/help/ru/gnome-text-editor/basics-create-new-file.page
/usr/share/help/ru/gnome-text-editor/basics-draft-folder.page
/usr/share/help/ru/gnome-text-editor/basics-open-file.page
/usr/share/help/ru/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/ru/gnome-text-editor/edit-undo-redo.page
/usr/share/help/ru/gnome-text-editor/index.page
/usr/share/help/ru/gnome-text-editor/legal.xml
/usr/share/help/ru/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/ru/gnome-text-editor/media/search-recent.png
/usr/share/help/sv/gnome-text-editor/basics-create-new-file.page
/usr/share/help/sv/gnome-text-editor/basics-draft-folder.page
/usr/share/help/sv/gnome-text-editor/basics-open-file.page
/usr/share/help/sv/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/sv/gnome-text-editor/edit-undo-redo.page
/usr/share/help/sv/gnome-text-editor/index.page
/usr/share/help/sv/gnome-text-editor/legal.xml
/usr/share/help/sv/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/sv/gnome-text-editor/media/search-recent.png
/usr/share/help/tr/gnome-text-editor/basics-create-new-file.page
/usr/share/help/tr/gnome-text-editor/basics-draft-folder.page
/usr/share/help/tr/gnome-text-editor/basics-open-file.page
/usr/share/help/tr/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/tr/gnome-text-editor/edit-undo-redo.page
/usr/share/help/tr/gnome-text-editor/index.page
/usr/share/help/tr/gnome-text-editor/legal.xml
/usr/share/help/tr/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/tr/gnome-text-editor/media/search-recent.png
/usr/share/help/uk/gnome-text-editor/basics-create-new-file.page
/usr/share/help/uk/gnome-text-editor/basics-draft-folder.page
/usr/share/help/uk/gnome-text-editor/basics-open-file.page
/usr/share/help/uk/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/uk/gnome-text-editor/edit-undo-redo.page
/usr/share/help/uk/gnome-text-editor/index.page
/usr/share/help/uk/gnome-text-editor/legal.xml
/usr/share/help/uk/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/uk/gnome-text-editor/media/search-recent.png
/usr/share/help/zh_CN/gnome-text-editor/basics-create-new-file.page
/usr/share/help/zh_CN/gnome-text-editor/basics-draft-folder.page
/usr/share/help/zh_CN/gnome-text-editor/basics-open-file.page
/usr/share/help/zh_CN/gnome-text-editor/edit-search-and-replace.page
/usr/share/help/zh_CN/gnome-text-editor/edit-undo-redo.page
/usr/share/help/zh_CN/gnome-text-editor/index.page
/usr/share/help/zh_CN/gnome-text-editor/legal.xml
/usr/share/help/zh_CN/gnome-text-editor/media/org.gnome.TextEditor.svg
/usr/share/help/zh_CN/gnome-text-editor/media/search-recent.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-text-editor/338650eb7a42dd9bc1f1c6961420f2633b24932d

%files locales -f gnome-text-editor.lang
%defattr(-,root,root,-)

