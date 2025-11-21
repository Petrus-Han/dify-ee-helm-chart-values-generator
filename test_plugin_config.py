#!/usr/bin/env python3
"""
测试脚本：交互测试插件配置模块
"""

import sys
import os

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 导入生成器类
import importlib.util
spec = importlib.util.spec_from_file_location("generate_values_prd", "generate-values-prd.py")
generate_values_prd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generate_values_prd)

ValuesGenerator = generate_values_prd.ValuesGenerator

def test_plugin_config():
    """测试插件配置"""
    print("=" * 60)
    print("测试插件配置模块")
    print("=" * 60)
    
    source_file = "values.yaml"
    
    if not os.path.exists(source_file):
        print(f"错误: 模板文件 {source_file} 不存在")
        return False
    
    # 创建生成器
    print(f"\n加载模板文件: {source_file}")
    generator = ValuesGenerator(source_file)
    
    # 测试插件配置
    print("\n" + "=" * 60)
    print("开始测试插件配置模块...")
    print("=" * 60)
    print("\n提示：请按照提示输入测试数据")
    print("建议测试流程：")
    print("  1. 选择 'y' 配置 Plugin Connector 镜像仓库")
    print("  2. 选择镜像仓库类型（docker 或 ecr）")
    print("  3. 如果选择 ecr，输入 ECR 区域")
    print("  4. 配置其他选项")
    print("\n开始测试...\n")
    
    try:
        generator.configure_plugins()
        
        # 显示配置结果
        print("\n" + "=" * 60)
        print("配置结果:")
        print("=" * 60)
        
        if 'plugin_connector' in generator.values:
            plugin_config = generator.values['plugin_connector']
            print("\nPlugin Connector 配置:")
            print(f"  镜像仓库类型: {plugin_config.get('imageRepoType', '未设置')}")
            if plugin_config.get('imageRepoType') == 'ecr':
                print(f"  ECR 区域: {plugin_config.get('ecrRegion', '未设置')}")
            print(f"  不使用 HTTPS: {plugin_config.get('insecureImageRepo', False)}")
            print(f"  Secret 名称: {plugin_config.get('imageRepoSecret', '未设置')}")
            print(f"  镜像仓库前缀: {plugin_config.get('imageRepoPrefix', '未设置')}")
        else:
            print("\n未配置 Plugin Connector 镜像仓库")
        
        print("\n✓ 测试完成！")
        return True
        
    except KeyboardInterrupt:
        print("\n\n用户中断测试")
        return False
    except Exception as e:
        print(f"\n✗ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_plugin_config()
    sys.exit(0 if success else 1)

