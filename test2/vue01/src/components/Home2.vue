<template>
<div id="magicalDragScene" class="mc-root mc-ui-absolute-pane">
	<el-container style="position: absolute; left: 16.5033%; top: 18.5714%;">
		<el-header height="55px">
			<el-breadcrumb separator="/">
				<el-breadcrumb-item>首页</el-breadcrumb-item>
				<el-breadcrumb-item>活动页</el-breadcrumb-item>
			</el-breadcrumb>
		</el-header>
		<el-container>
			<el-aside width="143px">
				<el-menu mode="vertical">
					<el-submenu index="1">
						<span class="magical-drag-tmp-submenu-name" slot="title">子菜单1</span>
						<el-menu-item index="1-1">菜单条目1-1</el-menu-item>
						<el-submenu index="1-2">
							<span class="magical-drag-tmp-submenu-name" slot="title">子菜单1-2</span>
							<el-menu-item index="1-2-1">菜单条目1-2-1</el-menu-item>
						</el-submenu>
					</el-submenu>
					<el-submenu index="2">
						<span class="magical-drag-tmp-submenu-name" slot="title">子菜单2</span>
						<el-menu-item index="2-1">菜单条目2-1</el-menu-item>
					</el-submenu>
					<el-menu-item index="3">菜单条目3</el-menu-item>
				</el-menu>
			</el-aside>
			<el-container>
				<el-main v-if="false"></el-main>
				<el-footer height="308px" v-if="true">
					<el-page-header content="详情页"></el-page-header>
					<el-table :data="tableList" :fit="true" :show-header="true">
						<el-table-column prop="id" label="列1"></el-table-column>
						<el-table-column prop="name" label="列2"></el-table-column>
						<el-table-column label="操作" fixed="right" width="200px">
							<template slot-scope="scope">
								<el-button mc-type="column-el-button" size="mini" type="primary">编辑</el-button>
								<el-button mc-type="column-el-button" size="mini" type="danger">删除</el-button>
							</template>
						</el-table-column>
					</el-table>
				</el-footer>
			</el-container>
		</el-container>
	</el-container>
</div>
</template>

<script>
export default {
  name: "Home2"
}
</script>

<style scoped>

</style>
